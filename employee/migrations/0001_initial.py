# Generated by Django 3.2.4 on 2021-06-29 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=35)),
                ('middle_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=35)),
                ('dob', models.CharField(max_length=50)),
                ('doj', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('flat_no', models.CharField(max_length=15)),
                ('st_name', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=8)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
    ]
