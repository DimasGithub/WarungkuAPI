from django.db import models

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
