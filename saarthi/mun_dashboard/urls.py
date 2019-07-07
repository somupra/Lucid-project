from django.urls import path
from .views import *

urlpatterns = [
<<<<<<< HEAD
    path('', dashboard, name = 'dashboard')
=======
    path('', dashboard, name = 'dashboard'),
    path('verify/<uuid:pk>', approve_success, name = 'verify'),
    path('mark_solved/<uuid:pk>', mark_solved, name = 'solved-success'),
    path('verified-complaints/', verified_complaints, name = 'verified-complaints'),
    path('solved-complaints/', solved_complaints, name = 'solved-complaints'),
>>>>>>> loginfeature
]