# Generated by Django 3.2.21 on 2023-10-15 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20231013_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='country',
        ),
    ]
