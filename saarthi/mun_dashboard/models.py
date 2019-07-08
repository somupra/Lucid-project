from django.db import models
from users.models import User
import uuid
# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length = 30)
    reward = models.IntegerField()

    def __str__(self):
        return self.title


class Complaint(models.Model):

    complaint_types = [
		('Accident', 'Accident'),
		('Potholes', 'Potholes'),
		('Landslides', 'Landslides'),
	]

    location = models.URLField()
    
    is_verified = models.BooleanField(default = False)
    is_settled = models.BooleanField(default = False)
    
    complaint_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    filer = models.ForeignKey(User, on_delete = models.CASCADE)
    
    date_filed = models.DateTimeField(auto_now_add = True, null = True)
    ref_image = models.ImageField(upload_to= 'Complaints', default = None)
    
    type_of_complaint = models.CharField(max_length = 9, choices = (('Accident','Accident'),('Disaster','Natural Disaster'),('Roads','Road Maintenance'),('Other','Other')))
    tag = models.ManyToManyField(Tag, related_name = 'complaints')
    
    description = models.TextField()
    complaint_status = models.CharField(max_length = 10)




