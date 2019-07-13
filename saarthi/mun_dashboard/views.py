from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from users.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import officials_only

@login_required
@officials_only
def welcome(request):
    return render(request, 'mun_dashboard/welcome.html')

@login_required
@officials_only
def dashboard(request):
    complaints = Complaint.objects.filter(is_verified = False).order_by('-date_filed')
    return render(request, 'mun_dashboard/dashboard.html', {'complaints': complaints})

@login_required
@officials_only
def decline(request, pk):
    complaint = get_object_or_404(Complaint, pk = pk)
    declinenotif = "Your complaint with ID "+ str(complaint.complaint_id)[:8] + " is declined"
    Notification.objects.create(user=complaint.filer, notification = declinenotif)
    complaint.delete()
    messages.success(request, f'Complaint deleted successfully!')
    return redirect('dashboard')

@login_required
@officials_only
def mark_spam(request, pk):
    complaint = get_object_or_404(Complaint, pk = pk)
    
    spamnotif = "Your complaint with ID "+ str(complaint.complaint_id)[:8] + " is marked as spam, this is a warning that you should file truthful complaints"
    Notification.objects.create(user=complaint.filer, notification = spamnotif)
    
    complaint.filer.profile.spamcount += 1
    
    if complaint.filer.profile.spamcount > 4 and complaint.filer.profile.spamcount % 5 == 0:
        complaint.filer.profile.rewards -= 10 
        deductionnotif = "Your complaint with ID "+ str(complaint.complaint_id)[:8] + " is marked as spam, and due to continuous spamming, a reward of 10 is deducted from your account"
        Notification.objects.create(user=complaint.filer, notification = deductionnotif)

    complaint.filer.profile.save()
    complaint.delete()
    messages.success(request, f'Complaint marked as spam successfully!')
    return redirect('dashboard')

@login_required
@officials_only
def approve_success(request, pk):
    complaint = get_object_or_404(Complaint, pk = pk)
    complaint.is_verified = True
    complaint.status = 'Verified'
    points = 10
    complaint.filer.profile.rewards += points
    complaint.filer.profile.save()
    complaint.save()
    approvenotif = "Your complaint with ID "+ str(complaint.complaint_id)[:8] + " is approved and reward of 10 is credited to your account. Thanks for bringing this to our notice."
    Notification.objects.create(user=complaint.filer, notification = approvenotif)
    messages.success(request, f'Complaint verified successfully!')
    return render(request, 'mun_dashboard/approved_complaint.html', {'complaint': complaint, 'reward': points})

@login_required
@officials_only
def mark_solved(request, pk):
    complaint = get_object_or_404(Complaint, pk = pk)
    complaint.is_settled = True
    complaint.status = 'Solved'
    complaint.save()
    successnotif = "Your complaint with ID "+ str(complaint.complaint_id)[:8] + " is settled, Keep helping us ahead."
    Notification.objects.create(user=complaint.filer, notification = successnotif)
    messages.success(request, f'Complaint marked solved successfully!')
    return render(request, 'mun_dashboard/solved_complaint.html', {'complaint': complaint})

@login_required
@officials_only
def verified_complaints(request):
    complaints = Complaint.objects.filter(is_verified = True, is_settled = False).order_by('-date_filed')
    return render(request, 'mun_dashboard/verified_complaints.html', {'complaints': complaints})

@login_required
@officials_only
def solved_complaints(request):
    complaints = Complaint.objects.filter(is_settled= True).order_by('-date_filed')
    return render(request, 'mun_dashboard/solved_complaints.html', {'complaints': complaints})





