# Generated by Django 2.2 on 2021-04-10 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210408_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='kode_pos',
        ),
    ]
