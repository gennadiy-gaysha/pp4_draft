# Generated by Django 3.2.21 on 2023-10-10 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20231010_1526'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='location',
            new_name='home_country',
        ),
    ]
