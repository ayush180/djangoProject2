from django.db import models
from django.urls import reverse
from category.models import category
from subcategory.models import subcategory
from material.models import material
# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=200)
    model_no = models.CharField(max_length=200)
    maincategory = models.ForeignKey(category, on_delete=models.CASCADE, related_name='category')
    size = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    materials = models.ForeignKey(material, on_delete=models.CASCADE, related_name='materials')
    quantity = models.IntegerField(default=0)
    subcat = models.ForeignKey(subcategory, on_delete=models.CASCADE, related_name='subcategory')
    product_comp_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("product-view")