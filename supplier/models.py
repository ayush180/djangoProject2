from django.db import models
from django.urls import reverse
# Create your models here.

class suppliers(models.Model):
    company_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=35)
    middle_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    phone = models.CharField(max_length=10)
    office_no = models.CharField(max_length=10)
    flat_no = models.CharField(max_length=15)
    st_name = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=8)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    gst = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    contact_person_name = models.CharField(max_length=100, null=True, blank=True)
    contact_person_phone = models.CharField(max_length=10, null=True, blank=True)
    remarks = models.TextField(null= True, blank= True)

    def __str__(self):
        return f"{self.company_name} "

    def get_absolute_url(self):
        return reverse("supplier-view")