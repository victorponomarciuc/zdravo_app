# Generated by Django 4.0 on 2022-08-14 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_services_category_alter_services_service_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='category',
            field=models.ManyToManyField(related_name='department_for_services', to='main.PersonalPostPosition', verbose_name='Категория'),
        ),
    ]
