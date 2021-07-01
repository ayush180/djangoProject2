from django.db import models
from django.urls import reverse
# Create your models here.
class OwnerPayment(models.Model):
    choice = (
        ('cash','cash'), ('netbank','netbank'), ('upi','upi'), ('cheque', 'cheque')
    )
    type = models.CharField(max_length=80, choices=choice)
    bank_name = models.CharField(max_length=80)
    bank_branch = models.CharField(max_length=400)
    account_no = models.CharField(max_length=80)
    ifsc_code = models.CharField(max_length=80)
    phone = models.CharField(max_length=15)
    upi = models.CharField(max_length=80)
    cash = models.IntegerField(default=0)
    check_no = models.CharField(max_length=30, default='')
    check_date = models.CharField(max_length=35, default='')
    balance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.bank_name} - {self.balance}"

    def get_absolute_url(self):
        return reverse("payment-view")