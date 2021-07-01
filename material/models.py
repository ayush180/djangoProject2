from django.db import models
from django.urls import reverse
# Create your models here.
class material(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(null= True, blank=True)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("material-view")
