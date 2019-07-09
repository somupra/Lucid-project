from django.urls import path
from .views import *

urlpatterns = [
    path('complaints/pending', ComPendingView.as_view(), name='pending'),
    path('complaints/verified', ComVerifiedView.as_view(), name='verified'),
    # path('complaints/create', ComCreateView.as_view(), name='create'),

]