# Generated by Django 3.2.4 on 2021-06-29 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_customer_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='doc',
            field=models.FileField(default='', upload_to='documents'),
        ),
        migrations.AddField(
            model_name='customer',
            name='photo',
            field=models.ImageField(blank=True, default='deafault.jpg', upload_to='photos'),
        ),
    ]
