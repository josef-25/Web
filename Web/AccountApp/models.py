from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

class Specialty(models.Model):
    name= models.ChartField(max_length=100)

class Doctor(User):
 license_number = model.ChartField(max_length=6, unique=True)
 phone = model.ChartField(max_length=8)
 specialties = models.ManyToManyField('Specialty' , related_name='doctors')
 

class Patient(User):
 national_id = models.CharField(max_length=8, unique=True)
 phone = models.CharField(max_length=8)
 birth_date = models.DateField()

