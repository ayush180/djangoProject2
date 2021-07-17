from django.db import models
from product.models import product
from datetime import datetime
from django.urls import reverse
# Create your models here.
class loss(models.Model):
    date = models.DateField(default=datetime.utcnow)
    product = models.ForeignKey(product, on_delete=models.CASCADE, related_name="loss")
    price = models.IntegerField()
    rate = models.IntegerField()
    quantity = models.IntegerField()
    remark = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}-{self.product}"

    def get_absolute_url(self):
        return reverse("loss-view")