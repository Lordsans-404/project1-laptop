# Generated by Django 3.2 on 2022-11-19 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_galleryimage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GalleryImage',
            new_name='ProductImage',
        ),
    ]