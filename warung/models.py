from django.db import models
from django.db.models.base import ModelState
from django.db.models.deletion import CASCADE

# Create your models here.
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
class Stocker(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name
class Goods(models.Model):
    name = models.CharField(max_length=70, blank=False)
    qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=CASCADE)
    purchase_price = models.IntegerField()
    purchase_perqty = models.IntegerField()
    billing_prince = models.IntegerField()
    purchase_date = models.DateField()
    stocker_name = models.ForeignKey(Stocker, on_delete=CASCADE)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.purchase_perqty = self.purchase_price / self.qty
        super(Goods, self).save(*args, **kwargs)

class Deposit(models.Model):
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    deposit_amount = models.IntegerField(default=0)
    amount_sold = models.IntegerField(default=0)
    billing_price = models.IntegerField()
    total = models.IntegerField(default=0)
    st = (
    ("SELESAI", "SELESAI"),
    ("BELUM SELESAI", "BELUM SELESAI"),)
    status = models.CharField(choices=st, default='BELUM SELESAI', max_length=20)
    