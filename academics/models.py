from django.db import models

# Create your models here.
class Studentacademics(models.Model):
    studentrollno=models.IntegerField(max_length=10)
    maths=models.IntegerField(max_length=100)
    physics=models.IntegerField(max_length=100)
    chemistry=models.IntegerField(max_length=100)
    biology=models.IntegerField(max_length=100)
    english=models.IntegerField(max_length=100)
