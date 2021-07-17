from django.db import models
from datetime import datetime
from prodoutward.models import prodoutward
from customer.models import customer
from django.urls import reverse

# Create your models here.

class outward_purchase(models.Model):
    date = models.DateField(default=datetime.utcnow)
    cus = models.ForeignKey(customer, on_delete=models.CASCADE, related_name="customers")
    products = models.ManyToManyField(prodoutward, related_name='outward_purchase_bill')
    total = models.IntegerField()
    gst = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    discount = models.DecimalField(default=0, max_digits=9, decimal_places=2, blank=True, null=True)
    net_amount = models.DecimalField(max_digits=9, decimal_places=2)
    due_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.id} "

    def get_absolute_url(self):
        return reverse('purchase-view')

