# Generated by Django 4.0.4 on 2022-05-27 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Pictures',
        ),
    ]