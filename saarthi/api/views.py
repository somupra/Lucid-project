from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication
from mun_dashboard.models import *
from .serializers import *

class ComCreateView(generics.CreateAPIView):
    
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (authentication.TokenAuthentication,)
    serializer_class = ComplaintSerializer

    def perform_create(self, serializer):
        print("I was here")
        serializer.save(filer=self.request.user)

class TrialCreateView(generics.CreateAPIView):

    def perform_create(self, serializer):
        print("I was here")
        serializer.save(filer=self.request.user)
    
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (authentication.TokenAuthentication,)
    serializer_class = TrialSerializer


class ComPendingView(generics.ListAPIView):
    
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (authentication.TokenAuthentication, )
    serializer_class = ComplaintSerializer

    def get_queryset(self, *args, **kwargs):
        return Complaint.objects.all().filter(filer=self.request.user, is_verified = False, is_settled = False)


class ComVerifiedView(generics.ListAPIView):
    
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (authentication.TokenAuthentication, )
    serializer_class = ComplaintSerializer

    def get_queryset(self, *args, **kwargs):
        return Complaint.objects.all().filter(filer = self.request.user, is_verified = True, is_settled = False)

class ComSettledView(generics.ListAPIView):
    
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication, )
    serializer_class = ComplaintSerializer

    def get_queryset(self, *args, **kwargs):
        return Complaint.objects.all().filter(filer = self.request.user, is_verified = True, is_settled = True)


class NotificationView(generics.ListAPIView):
    
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (authentication.TokenAuthentication, )
    serializer_class = NotificationSerializer

    def get_queryset(self, *args, **kwargs):
        return Notification.objects.all().filter(user = self.request.user)

