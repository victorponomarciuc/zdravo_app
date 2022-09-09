# Generated by Django 4.0 on 2022-08-20 13:17

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_alter_checkupitems_slug_alter_department_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='description',
            field=django_quill.fields.QuillField(blank=True, null=True, verbose_name='Описание отделения'),
        ),
        migrations.AlterField(
            model_name='services',
            name='service_type',
            field=models.CharField(choices=[('consult', 'Консультация'), ('diagnostic', 'Диангостика'), ('service', 'Услуга'), ('service_analisys', 'Анализы')], default='consult', max_length=50, verbose_name='Тип Услуги'),
        ),
    ]