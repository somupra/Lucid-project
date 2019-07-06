from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    complaints = Complaint.objects.filter(is_verified = False).order_by('-date_filed')
    return render(request, 'mun_dashboard/dashboard.html', {'complaints': complaints})

@login_required
def approve_success(request, pk):
    complaint = Complaint.objects.get(pk = pk)
    complaint.is_verified = True
    points = 0
    for reward in complaint.tags.reward:
        points += reward
    complaint.filer.profile.rewards = points
    return render('mun_dashboard/approved_complaint.html', {'complaint': complaint, 'reward': points})

@login_required
def marksolved(request, pk):
    complaint = Complaint.objects.get(pk = pk)
    complaint.is_settled = True
    return redirect('verified-complaints')

@login_required
def verifiedcomplaints(request):
    complaints = Complaint.objects.filter(is_verified = True).order_by('-date_filed')
    return render(request, 'mun_dashboard/verified_complaints.html', {'complaints': complaints})

@login_required
def solvedcomplaints(request):
    complaints = Complaint.objects.filter(is_settled= True).order_by('-date_filed')
    return render(request, 'mun_dashboard/solved_complaints.html', {'complaints': complaints})

# @login_required
# def confirm_verification(request, pk):
#     complaint = get_object_or_404(Complaint, pk = pk)
#     return render()




