from django.db import models
from django.urls import reverse
from product.models import product
# Create your models here.
class prodoutward(models.Model):
    prod = models.ForeignKey(product, on_delete=models.CASCADE, related_name="products")
    quantity = models.IntegerField(default=0)
    rate = models.FloatField(max_length=100)
    price = models.FloatField(max_length=100)
    discount = models.FloatField(default=0, max_length=100, blank=True, null=True)
    gst = models.FloatField(default=0,max_length=100, blank=True, null=True)
    is_billed = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.price}"

    def get_absolute_url(self):
        return reverse("close")