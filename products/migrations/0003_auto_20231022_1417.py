# Generated by Django 3.2.21 on 2023-10-22 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_subcategory_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categorie'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'Subcategorie'},
        ),
    ]