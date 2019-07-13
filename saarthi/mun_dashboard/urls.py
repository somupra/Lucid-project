from django.urls import path
from .views import *

urlpatterns = [
    path('', welcome, name = 'welcome'),
    path('/dashboard', dashboard, name = 'dashboard'),
    path('verify/<uuid:pk>', approve_success, name = 'verify'),
    path('decline/<uuid:pk>', decline, name = 'decline'),
    path('spam/<uuid:pk>', mark_spam, name = 'spam'),
    path('mark_solved/<uuid:pk>', mark_solved, name = 'solved-success'),
    path('verified-complaints/', verified_complaints, name = 'verified-complaints'),
    path('solved-complaints/', solved_complaints, name = 'solved-complaints'),
]