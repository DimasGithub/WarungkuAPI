from django.db import models
from django.db.models.base import ModelState
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from warung.models import good

class Debt(models.Model):
    date = models.DateField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_debt = models.ForeignKey(good, on_delete=models.CASCADE, max_length=70)
    qty = models.IntegerField()
    note = models.TextField(blank=True)
    total_debt = models.IntegerField()
    def __str__(self):
        return self.name_debt.name
    def save(self, *args, **kwargs):
        self.name_debt.qty - self.qty
        self.total_sold = self.name_debt.billing_prince * self.qty
        super(Debt, self).save(*args, **kwargs)