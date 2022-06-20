from django.db import models
from django.forms import widgets

#from django.db.models.fields.related import ForeignKey
# Create your models here.


class StudentList(models.Model):
    First_Name = models.CharField(max_length=15, blank=False)
    Last_Name = models.CharField(max_length=10, blank=False)
    Address = models.CharField(max_length=20, blank=False)
    cell = models.CharField(max_length=12, blank=False)
