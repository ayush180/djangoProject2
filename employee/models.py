from django.db import models
from django.urls import reverse
# Create your models here.
class employee(models.Model):
    choice = (
        ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')
    )
    first_name = models.CharField(max_length=35)
    middle_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    dob = models.CharField(max_length=50)
    doj = models.CharField(max_length=50)
    post = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=20, choices=choice )
    flat_no = models.CharField(max_length=15)
    st_name = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=8)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos',blank=True,default='default.jpg')
    doc = models.FileField(upload_to='documents', default='')

    def __str__(self):
        return f"{self.first_name} "

    def get_absolute_url(self):
        return reverse("employee-view")