# Generated by Django 3.2.21 on 2023-10-16 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20231016_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='phone',
            field=models.CharField(default='', max_length=100),
        ),
    ]
