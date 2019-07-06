from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Complaint(models.Model):

    complaint_types = [
		('Accident', 'Accident'),
		('Potholes', 'Potholes'),
		('Landslides', 'Landslides'),
	]

    location = models.TextField()
    is_verified = models.BooleanField(default = False)
    is_settled = models.BooleanField(default = False)
    complaint_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    filer = models.ForeignKey(User, on_delete = models.CASCADE)
    date_filed = models.DateField(auto_now_add= True)
    ref_image = models.ImageField(upload_to= 'Complaints', default = None)
    tag = models.CharField(max_length = 9, choices = (('Accident','Accident'),('Disaster','Natural Disaster'),('Roads','Road Maintenance'),('Other','Other')))
    description = models.TextField()
    complaint_status = models.CharField(max_length = 10)

class Tag(models.Model):
    complaint = models.ManyToManyField(Complaint, related_name = 'tags')
    title = models.CharField(max_length = 30)
    reward = models.IntegerField()
