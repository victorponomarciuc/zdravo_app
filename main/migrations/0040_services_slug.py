# Generated by Django 4.0 on 2022-08-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_remove_services_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='slug',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]