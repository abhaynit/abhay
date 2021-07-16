from django.db import models

# Create your models here.
class student(models.Model):
    reg_no=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    image = models.ImageField(upload_to="myimage")
