from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication
from mun_dashboard.models import *
from .serializers import *

# class ComCreateView(generics.ListAPIView):
    
#     permission_classes = (IsOwner)

#     def post(self, request):
#         queryset = Complaint.objects.(filer = request.user)
#         return Response(content)


class ComPendingView(generics.ListAPIView):
    
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (authentication.TokenAuthentication, )
    serializer_class = ComplaintSerializer

    def get_queryset(self, *args, **kwargs):
     return Complaint.objects.all().filter(filer=self.request.user, is_verified = False, is_settled = False)


class ComVerifiedView(generics.ListAPIView):
    
    permission_classes = (IsAuthenticated,)
    serializer_class = ComplaintSerializer

    def get_queryset(self, *args, **kwargs):
     return Complaint.objects.all().filter(filer=self.request.user, is_verified = True, is_settled = False)

class ComSettledView(generics.ListAPIView):
    
    permission_classes = (IsAuthenticated,)
    serializer_class = ComplaintSerializer

    def get_queryset(self, *args, **kwargs):
     return Complaint.objects.all().filter(filer=self.request.user, is_verified = True, is_settled = True)

