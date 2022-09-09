# Generated by Django 4.0 on 2022-08-10 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_aboutsection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutsection',
            name='title',
        ),
        migrations.AddField(
            model_name='aboutsection',
            name='title_1',
            field=models.CharField(default='Заголовок 1', max_length=100, verbose_name='Заголовок 1'),
        ),
        migrations.AddField(
            model_name='aboutsection',
            name='title_2',
            field=models.CharField(default='Заголовок 2', max_length=100, verbose_name='Заголовок 2'),
        ),
    ]