# Generated by Django 4.0 on 2022-08-20 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_services_slug_alter_checkupitems_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='slug',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
