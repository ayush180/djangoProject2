from django.db import models
from django.urls import  reverse
from category.models import category
# Create your models here.
class subcategory(models.Model):
    name=models.CharField(max_length=80)
    description=models.TextField(null=True,blank=True)
    maincategory = models.ForeignKey(category, on_delete=models.CASCADE, related_name='subcategory')

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("subcategory-view")