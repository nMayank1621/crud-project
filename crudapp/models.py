from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)