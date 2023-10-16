# Generated by Django 3.2.21 on 2023-10-15 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.country'),
        ),
    ]
