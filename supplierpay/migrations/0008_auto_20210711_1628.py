# Generated by Django 3.2.4 on 2021-07-11 10:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inward_purchase', '0001_initial'),
        ('supplierpay', '0007_remove_suppayment_bill'),
    ]

    operations = [
        migrations.AddField(
            model_name='suppayment',
            name='bills',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='bills', to='inward_purchase.inward_purchase'),
        ),
        migrations.AddField(
            model_name='suppayment',
            name='dates',
            field=models.DateField(default=datetime.datetime.utcnow),
        ),
    ]
