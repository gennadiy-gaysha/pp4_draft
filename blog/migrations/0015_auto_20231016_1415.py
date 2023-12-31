# Generated by Django 3.2.21 on 2023-10-16 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20231016_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='area_sq_km',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='country',
            name='continent',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='country',
            name='currency_code',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='country',
            name='currency_name',
            field=models.CharField(default='', max_length=100),
        ),
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
        migrations.AddField(
            model_name='country',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='country',
            name='population',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='country',
            name='postal_code_format',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='country',
            name='postal_code_regex',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='country',
            name='tld',
            field=models.CharField(blank=True, default='', max_length=5),
        ),
    ]
