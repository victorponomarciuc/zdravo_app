# Generated by Django 4.0 on 2022-08-20 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_services_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='slug',
            field=models.CharField(default=models.CharField(max_length=100, verbose_name='Заголовок'), max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='checkupitems',
            name='slug',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='slug',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='personalpostposition',
            name='slug',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
