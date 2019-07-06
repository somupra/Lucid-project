from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name = 'dashboard'),
    path('verify/<uuid:pk>', approve_success, name = 'verify'),
    path('mark_solved/<uuid:pk>', marksolved, name = 'mark-solved'),
    path('verified-complaints/', verifiedcomplaints, name = 'verified-complaints'),
    path('solved-complaints/', solvedcomplaints, name = 'solved-complaints'),
]