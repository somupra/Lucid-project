from rest_framework import serializers
from mun_dashboard.models import *
from users.models import *

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('pk','title')


class ComplaintSerializer(serializers.ModelSerializer):
    
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
            'type_of_complaint',
            'tag',
            'description',
            'complaint_status'
        )



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