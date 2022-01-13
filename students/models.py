from django.db import models


# Create your models here.
class Student(models.Model):
    studentrollno=models.IntegerField(primary_key=True)
    studentname=models.CharField(max_length=39)
    studentclass=models.IntegerField(max_length=15)
    school=models.CharField(max_length=40)
    mobile=models.IntegerField(max_length=20)
    address=models.CharField(max_length=50)
    