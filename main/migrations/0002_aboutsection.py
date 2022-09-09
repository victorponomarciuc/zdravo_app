# Generated by Django 4.0 on 2022-08-10 18:48

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_left', models.FileField(upload_to='site_media', verbose_name='Изображение 1')),
                ('description_small', models.TextField(verbose_name='Описание 1')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('subtitle', models.CharField(max_length=100, verbose_name='Подзаголовок')),
                ('description_about', django_quill.fields.QuillField(verbose_name='Описание 2')),
                ('image_right', models.FileField(upload_to='site_media', verbose_name='Изображение 2')),
            ],
            options={
                'verbose_name': 'Секция Про Клинику',
                'verbose_name_plural': 'Секция Про Клинику',
            },
        ),
    ]
