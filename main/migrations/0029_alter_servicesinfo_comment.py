# Generated by Django 4.0 on 2022-08-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_servicesinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicesinfo',
            name='comment',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Контент'),
        ),
    ]
