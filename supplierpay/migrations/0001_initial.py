# Generated by Django 3.2.4 on 2021-07-01 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='suppayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('cash', 'cash'), ('netbank', 'netbank'), ('upi', 'upi'), ('cheque', 'cheque')], max_length=80)),
                ('bank_name', models.CharField(max_length=80)),
                ('bank_branch', models.CharField(max_length=400)),
                ('account_no', models.CharField(max_length=80)),
                ('ifsc_code', models.CharField(max_length=80)),
                ('phone', models.CharField(max_length=15)),
                ('upi', models.CharField(max_length=80)),
                ('cash', models.IntegerField(default=0)),
                ('check_no', models.CharField(default='', max_length=30)),
                ('check_date', models.CharField(default='', max_length=35)),
                ('sup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier', to='supplier.suppliers')),
            ],
        ),
    ]
