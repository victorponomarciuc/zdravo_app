# Generated by Django 4.0 on 2022-08-21 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_services_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(choices=[('consult', 'Консультация'), ('diagnostic', 'Диангостика'), ('service', 'Услуга'), ('service_analisys', 'Анализы')], default='consult', max_length=50, verbose_name='Тип Услуги')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('status', models.CharField(choices=[('new', 'Нова'), ('processing', 'В обробці'), ('complete', 'Завершено')], default='new', max_length=50, verbose_name='Статус')),
                ('date_created', models.DateField(blank=True, null=True, verbose_name='Дата отправки')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.clients', verbose_name='Клиент')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.services', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Заявки (Онлайн записи)',
                'verbose_name_plural': 'Заявки (Онлайн записи)',
            },
        ),
    ]
