# Generated by Django 3.2.4 on 2021-06-30 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('material', '0001_initial'),
        ('category', '0001_initial'),
        ('subcategory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('model_no', models.CharField(max_length=200)),
                ('size', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=200)),
                ('product_comp_name', models.CharField(max_length=200)),
                ('maincategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='category.category')),
                ('materials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='material.material')),
                ('subcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='subcategory.subcategory')),
            ],
        ),
    ]
