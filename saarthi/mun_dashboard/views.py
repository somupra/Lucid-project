from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def dashboard(request):
    complaints = Complaint.objects.all().order_by('date_filed')
    return render(request, 'mun_dashboard/dashboard.html', {'complaints': complaints})
