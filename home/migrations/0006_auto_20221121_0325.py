# Generated by Django 3.2 on 2022-11-21 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_galleryimage_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='img_product1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='img_product2',
        ),
    ]