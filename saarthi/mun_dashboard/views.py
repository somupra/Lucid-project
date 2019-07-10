from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import officials_only

# Create your views here.
@login_required
@officials_only
def dashboard(request):
    complaints = Complaint.objects.filter(is_verified = False).order_by('-date_filed')
    return render(request, 'mun_dashboard/dashboard.html', {'complaints': complaints})

@login_required
@officials_only
def approve_success(request, pk):
    complaint = get_object_or_404(Complaint, pk = pk)
    complaint.is_verified = True
    complaint.status = 'Verified'
    current_date = complaint.date_filed 
    complaint.date_filed = current_date
    points = 0
    for tag in complaint.tag.all():
        points += tag.reward
    complaint.filer.profile.rewards = points
    complaint.filer.profile.save()
    complaint.save()
    messages.success(request, f'Complaint verified successfully!')
    return render(request, 'mun_dashboard/approved_complaint.html', {'complaint': complaint, 'reward': points})

@login_required
@officials_only
def mark_solved(request, pk):
    complaint = get_object_or_404(Complaint, pk = pk)
    complaint.is_settled = True
    complaint.status = 'Solved'
    complaint.save()
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





