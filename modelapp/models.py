from django.db import models
from django.db.models.base import Model
from django.utils import timezone
class Musician(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    instrument=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.first_name

class Album(models.Model):
    artist=models.ForeignKey(Musician,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    release_data=models.DateField(default=timezone.now)
    def __str__(self) -> str:
        return self.name
