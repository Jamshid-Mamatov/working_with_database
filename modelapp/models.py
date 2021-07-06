from django.db import models
from django.db.models.base import Model


class Person(models.Model):
    shirt_sizes=[
        ('l','Large'),
        ('m','Medium'),
        ('s','Small'),

    ]
    name=models.CharField(max_length=10)
    shirt_size=models.CharField(max_length=1,choices=shirt_sizes)
    def __str__(self) -> str:
        return self.name
        
