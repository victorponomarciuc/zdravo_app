# Generated by Django 4.0 on 2022-08-14 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_contactsinformation_telegram_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='category',
            field=models.ManyToManyField(related_name='department_for_services', to='main.PersonalPostPosition', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='services',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Цена услуги'),
        ),
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='site_media', verbose_name='Изображение'),
        ),
    ]