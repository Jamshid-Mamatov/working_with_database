from django.db import models
from django.db.models.base import Model

class Language(models.Model):
    name=models.CharField(max_length=10)

class Framework(models.Model):
    name=models.CharField(max_length=10)
    language=models.ForeignKey(Language,on_delete=models.CASCADE)
    