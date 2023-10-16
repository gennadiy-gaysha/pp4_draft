# Generated by Django 3.2.21 on 2023-10-15 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='area_sq_km',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='country',
            name='capital',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='country',
            name='continent',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='country',
            name='currency_code',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='country',
            name='currency_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='country',
            name='equivalent_fips_code',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='country',
            name='fips',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='country',
            name='geonameid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='country',
            name='iso',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AddField(
            model_name='country',
            name='iso3',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AddField(
            model_name='country',
            name='iso_numeric',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AddField(
            model_name='country',
            name='neighbours',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='country',
            name='phone',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='country',
            name='population',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='country',
            name='postal_code_format',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='country',
            name='postal_code_regex',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='country',
            name='tld',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='country',
            name='country_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='blog.country')),
            ],
        ),
    ]
