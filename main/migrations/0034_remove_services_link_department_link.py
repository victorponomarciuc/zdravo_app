# Generated by Django 4.0 on 2022-08-20 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_remove_services_image_department_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='link',
        ),
        migrations.AddField(
            model_name='department',
            name='link',
            field=models.CharField(default='#', max_length=100, verbose_name='Ссылка'),
        ),
    ]
