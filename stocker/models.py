from django.db import models
from django.db.models.base import ModelState
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

class Stocker(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name

# Create your models here.
