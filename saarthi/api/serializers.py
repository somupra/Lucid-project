from rest_framework import serializers
from mun_dashboard.models import *
from users.models import *
# from drf_extra_fields.fields import Base64ImageField
from .functions import Base64ImageField

class TrialSerializer(serializers.ModelSerializer):
    
    image = Base64ImageField(
        max_length=None, use_url=True,
    )
    class Meta:
        model = TrialModel
        fields = ('image', 'name')


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('pk','title')


class ComplaintSerializer(serializers.ModelSerializer):

    ref_image= Base64ImageField(
        max_length=None, use_url=True,
    )

    tag = serializers.StringRelatedField(many = True)
    
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