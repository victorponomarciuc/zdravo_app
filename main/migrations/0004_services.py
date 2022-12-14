# Generated by Django 4.0 on 2022-08-10 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_aboutsection_title_aboutsection_title_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='site_media', verbose_name='Изображение')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('link', models.CharField(max_length=100, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
