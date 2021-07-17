from django.db import models
from django.urls import reverse
from inward_purchase.models import inward_purchase
from datetime import datetime
# Create your models here.
class suppayment(models.Model):
    choice = (
        ('cash','cash'), ('netbank','netbank'), ('upi','upi'), ('cheque', 'cheque')
    )
    type = models.CharField(max_length=80, choices=choice)
    dates = models.DateField(default=datetime.utcnow)
    bank_name = models.CharField(max_length=80, null=True, blank=True)
    bank_branch = models.CharField(max_length=400, null=True, blank=True)
    account_no = models.CharField(max_length=80, null=True, blank=True)
    ifsc_code = models.CharField(max_length=80, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    upi = models.CharField(max_length=80, null=True, blank=True)
    cash = models.IntegerField(default=0,null=True, blank=True)
    check_no = models.CharField(max_length=30, default='', null=True, blank=True)
    check_date = models.CharField(max_length=35, default='', null=True, blank=True)
    bills = models.ForeignKey(inward_purchase, on_delete=models.CASCADE, related_name="bills", default='')

    def __str__(self):
        return f"{self.type}"

    def get_absolute_url(self):
        return reverse("supplierpay-view")