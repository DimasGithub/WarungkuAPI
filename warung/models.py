from django.db import models
from django.db.models.base import ModelState
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
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
    def __str__ (self):
        return self.name
class Sold(models.Model):
    date = models.DateField(auto_now_add = True)
    name_sold = models.ForeignKey(Goods, on_delete=models.CASCADE, max_length=70)
    qty = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_sold = models.IntegerField()
    def __str__(self):
        return self.name_sold.qty
    def save(self, *args, **kwargs):
        self.total_sold = self.name_sold.billing_prince * self.qty
        super(Sold, self).save(*args, **kwargs)

class Debt(models.Model):
    date = models.DateField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_debt = models.ForeignKey(Goods, on_delete=models.CASCADE, max_length=70)
    qty = models.IntegerField()
    note = models.TextField(blank=True)
    total_debt = models.IntegerField()
    def __str__(self):
        return self.name_debt.name
    def save(self, *args, **kwargs):
        self.name_debt.qty - self.qty
        self.total_sold = self.name_debt.billing_prince * self.qty
        super(Debt, self).save(*args, **kwargs)
        
