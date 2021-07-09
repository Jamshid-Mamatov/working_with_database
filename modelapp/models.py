from django.db import models
from django.db.models.base import Model
from django.utils import timezone


class University(models.Model):
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.name

class Students(models.Model):
    name=models.CharField(max_length=10)
    university_name=models.ForeignKey(University,on_delete=models.CASCADE)
    course=models.CharField(max_length=1)
    date_birth=models.DateField(default=timezone.now)
    def __str__(self) -> str:
        return self.name
