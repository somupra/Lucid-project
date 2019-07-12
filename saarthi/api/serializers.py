from rest_framework import serializers
from mun_dashboard.models import *
from users.models import *
from .functions import Base64ImageField

class TrialSerializer(serializers.ModelSerializer):
    
    image = Base64ImageField(
        max_length=None, use_url=True,
    )
    class Meta:
        model = TrialModel
        fields = ('image', 'name')

class ComplaintSerializer(serializers.ModelSerializer):

    ref_image= Base64ImageField(
        max_length=None, use_url=True,
    )
    
    class Meta:
        model = Complaint
        fields = (
            'location',
            'is_verified',
            'is_settled',
            'complaint_id',
            'filer',
            'date_filed',
            'ref_image',
            'description',
            'complaint_status'
        )

    def create(self, validated_data):
        return Complaint.objects.create(filer = self.request.user, **validated_data)



class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = (
            'notification',
            'user',
        )

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'user',
            'rewards',
            'spamcount',
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'is_official',
        )