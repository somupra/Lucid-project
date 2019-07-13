from django.urls import path
from .views import *

urlpatterns = [
    path('complaints/pending', ComPendingView.as_view(), name='pending'),
    path('user/notifications/', NotificationView.as_view(), name='notifications'),
    path('complaints/verified', ComVerifiedView.as_view(), name='verified'),
    path('complaints/settled', ComSettledView.as_view(), name='settled'),
    path('complaints/create/', ComCreateView.as_view(), name='create'),
    path('uploadtrial/', TrialCreateView.as_view(), name='trialcreate'),
]