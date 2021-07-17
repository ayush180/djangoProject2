from django.db import models
from django.urls import reverse
# Create your models here.

class customer(models.Model):
    choice = (
        ('Male', 'Male'), ('Female', 'Female'), ('Other','Other')
    )
    company_name = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=35)
    middle_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    phone = models.CharField(max_length=10)
    dob = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photos',blank=True,default='default.jpg')
    doc = models.FileField(upload_to='documents', default='')

    gender = models.CharField(max_length=20, choices=choice)
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
        return f"{self.first_name} "

    def get_absolute_url(self):
        return reverse("customer-view")