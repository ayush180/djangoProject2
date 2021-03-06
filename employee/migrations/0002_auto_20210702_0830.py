# Generated by Django 3.2.4 on 2021-07-02 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='doc',
            field=models.FileField(default='', upload_to='documents'),
        ),
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20),
        ),
    ]
