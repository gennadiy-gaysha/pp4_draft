# Generated by Django 3.2.21 on 2023-10-16 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20231016_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='country',
            name='neighbours',
        ),
    ]
