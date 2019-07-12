from django.db import models
from users.models import User
import uuid
# Create your models here.

class TrialModel(models.Model):
    image = models.ImageField(upload_to = 'Compalints', default = None)
    name = models.CharField(max_length = 100)
    filer = models.ForeignKey(User, on_delete = models.CASCADE)

class Complaint(models.Model):

    location = models.CharField(max_length = 100)
    
    is_verified = models.BooleanField(default = False)
    is_settled = models.BooleanField(default = False)
    
    complaint_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    filer = models.ForeignKey(User, on_delete = models.CASCADE)
    
    date_filed = models.DateTimeField(auto_now_add = True, null = True)
    ref_image = models.ImageField(upload_to= 'Complaints', default = None)
        
    description = models.TextField()
    complaint_status = models.CharField(max_length = 10, default = 'pending')




