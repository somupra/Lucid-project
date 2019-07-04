from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def municipal_corporation(request):
	return render(request, 'municipality_dashboard/dashboard.html')

def info(request):
	return render(request,'municipality_dashboard/info.html')


