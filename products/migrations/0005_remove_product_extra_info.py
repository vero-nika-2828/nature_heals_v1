# Generated by Django 3.2.21 on 2024-01-10 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_extra_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='extra_info',
        ),
    ]
