from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    pan_number = models.CharField(max_length=10)
    pan_image = models.ImageField(upload_to='user',blank=True)
    dob = models.DateField()


class FileUpload(models.Model):
    file = models.ImageField(upload_to='user')
