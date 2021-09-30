from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class BioToko(models.Model):
    name = models.CharField(max_length=70, blank=False)
    author = models.CharField(max_length=70)
    location = models.CharField(max_length=100)
class Category(models.Model):
    name = models.CharField(max_length= 25)
class Stocker(models.Model):
    name = models.CharField(max_length=25)
    
class Goods(models.Model):
    name = models.CharField(max_length=70, blank=False)
    qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=CASCADE)
    purchase_price = models.IntegerField()
    billing_prince = models.IntegerField()
    purchase_date = models.DateField()
    billing_date  = models.DateField()
    stocker_name = models.ForeignKey(Stocker, on_delete=CASCADE)
