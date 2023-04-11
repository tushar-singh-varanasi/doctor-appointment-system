from django.db import models 
from django.contrib.auth.models import User 


# Create your models here.
class Contact(models.Model):
    Name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    message=models.TextField()

Doctor_CHOICES =(
    ('Orthopedics','Orthopedics'),
    ('Internal Medicine','Internal Medicine'),
    ('Obstetrics and Gynecology','Obstetrics and Gynecology'),
    ('Dermatology', 'Dermatology'),
    ('Pediatrics','Pediatric'),
    ('Radiology',' Radiology'),
    ('General Surgery',' General Surgery'),
    ('Ophthalmology','Ophthalmolog')




)

Gender_CHOICES=(
    ('Male','male'),
    ('Female','Female')
)

class Appointment(models.Model):
    Gender=models.CharField(choices=Gender_CHOICES,max_length=100)
    Age=models.IntegerField()
    Medical_Specialties=models.CharField(choices=Doctor_CHOICES,max_length=500)
    Date_and_time=models.DateTimeField()
    Patient_detail=models.ForeignKey(User,null=True,on_delete=models.CASCADE)

    

    