from django.shortcuts import render
from .models import *

# Create your views here.

def dashboard(request):
    complaints = Complaint.objects.all().order_by('date_filed')
    return render(request, 'mun_dashboard/dashboard.html', {'complaints': complaints})
