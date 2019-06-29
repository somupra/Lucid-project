from django.shortcuts import render

def passed_login(request):
    return render(request, 'User/test.html')

# Create your views here.
