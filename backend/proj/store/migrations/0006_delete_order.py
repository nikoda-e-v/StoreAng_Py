# Generated by Django 3.0.5 on 2021-06-15 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
