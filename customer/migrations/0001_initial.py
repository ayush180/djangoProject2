# Generated by Django 3.2.4 on 2021-06-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=35)),
                ('middle_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=35)),
                ('phone', models.CharField(max_length=10)),
                ('dob', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('flat_no', models.CharField(max_length=15)),
                ('st_name', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=8)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('gst', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('contact_person_name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_person_phone', models.CharField(blank=True, max_length=10, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
            ],
        ),
    ]