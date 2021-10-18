from django.db import models
from django.db.models.base import ModelState
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from stocker.models import Stocker

class BioToko(models.Model):
    name = models.CharField(max_length=70, blank=False)
    author = models.CharField(max_length=70)
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length= 25)
    def __str__(self):
        return self.name

class good(models.Model):
    name = models.CharField(max_length=70, blank=False)
    qty = models.IntegerField(default=0)
    category = models.ForeignKey(Category, related_name='dataku', on_delete=models.CASCADE)
    purchase_price = models.IntegerField()
    purchase_perqty = models.IntegerField()
    billing_prince = models.IntegerField()
    purchase_date = models.DateField()
    item_sold = models.IntegerField(default=0)
    stocker_name = models.ForeignKey(Stocker, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.qty = self.qty - self.item_sold
        self.purchase_perqty = self.purchase_price / self.qty
        super(good, self).save(*args, **kwargs)

# class Sold(models.Model):
#     date = models.DateField(auto_now_add = True)
#     name_sold = models.ForeignKey(good, on_delete=models.CASCADE, max_length=70)
#     qty = models.IntegerField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     total_sold = models.IntegerField()
#     def __str__(self):
#         return self.name_sold.qty
#     def save(self, *args, **kwargs):
#         self.total_sold = self.name_sold.billing_prince * self.qty
#         super(Sold, self).save(*args, **kwargs)

