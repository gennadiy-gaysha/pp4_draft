# Generated by Django 3.2.21 on 2023-10-16 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20231016_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='geonameid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='country',
            name='languages',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='country',
            name='neighbours',
            field=models.CharField(default='', max_length=100),
        ),
    ]
