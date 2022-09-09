import datetime

from django.core.exceptions import ValidationError
from django.db import models

from django_quill.fields import QuillField
from main.utils import enums
from slugify import slugify


class AvantagesSection(models.Model):
    image = models.FileField(upload_to='site_media', verbose_name="Изображение")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    display_order = models.IntegerField(verbose_name="Положение в списке", default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Преимущество компании'
        verbose_name_plural = "Преимущества компании"


class AboutSection(models.Model):
    image_left = models.FileField(upload_to='site_media', verbose_name="Изображение 1")
    title_1 = models.CharField(max_length=100, verbose_name="Заголовок 1", default="Заголовок 1")
    description_small = models.TextField(verbose_name="Описание 1")
    title_2 = models.CharField(max_length=100, verbose_name="Заголовок 2", default="Заголовок 2")
    subtitle = models.CharField(max_length=100, verbose_name="Подзаголовок")
    description_about = QuillField(verbose_name="Описание 2")
    image_right = models.FileField(upload_to='site_media', verbose_name="Изображение 2")

    def __str__(self):
        return "Контент для секции О Нас"

    class Meta:
        verbose_name = 'Секция Про Клинику'
        verbose_name_plural = "Секция Про Клинику"


class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название Отделения")
    image = models.FileField(upload_to='site_media', verbose_name="Изображение (Не обязательно)", null=True, blank=True)
    description = QuillField(verbose_name="Описание отделения", null=True, blank=True)
    slug = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.name).lower().replace(' ', '-'))
        super(Department, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Отделение'
        verbose_name_plural = "Отделения"


class PersonalPostPosition(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название Вакансии")
    department = models.ManyToManyField(Department, related_name="department_for_post", verbose_name="Отделения")
    slug = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.name).lower().replace(' ', '-'))
        super(PersonalPostPosition, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = "Вакансии"


class MedicalPersonal(models.Model):
    image = models.FileField(upload_to='site_media', verbose_name="Изображение")
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    experience = models.IntegerField(verbose_name="Стаж работы (лет)")
    post = models.ManyToManyField(PersonalPostPosition, related_name="department_for_personal_post",
                                  verbose_name="Вакансии")
    category_steep = models.CharField(max_length=50, choices=enums.PersonalCategorySTEP.choices,
                                      default=enums.PersonalCategorySTEP.INTERN, verbose_name="Категория")
    phone = models.CharField(max_length=100, verbose_name="Телефон", null=True, blank=True)
    comment = models.TextField(verbose_name="Комментарий", null=True, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = "Персонал"


class CheckUp(models.Model):
    comment = models.TextField(verbose_name="Контент", null=True, blank=True)
    image = models.FileField(upload_to='site_media', verbose_name="Изображение")

    def __str__(self):
        return "Check-UP информация"

    class Meta:
        verbose_name = 'Check-Up Информация'
        verbose_name_plural = "Check-Up Информация"


class CheckUpItems(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название Check-UP")
    image = models.FileField(upload_to='site_media', verbose_name="Картинка Check-UP")
    header_title = models.CharField(max_length=100, verbose_name="Заголовок хедера")
    header_image = models.FileField(upload_to='site_media', verbose_name="Картинка хедера")
    description = models.TextField(verbose_name="Описание Check-UP")
    content_title = models.CharField(max_length=100, verbose_name="Заголовок Check-UP")
    content = QuillField(verbose_name="Контент")
    display_order = models.IntegerField(verbose_name="Положение в списке", default=1)
    slug = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.title).lower().replace(' ', '-'))
        super(CheckUpItems, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Check-Up'
        verbose_name_plural = "Check-Up"


class ContactsInformation(models.Model):
    phone = models.CharField(max_length=100, verbose_name="Телефон")
    mail = models.CharField(max_length=100, verbose_name="Эл. Почта")
    address = models.CharField(max_length=255, verbose_name="Адресс")
    geolocation = models.TextField(verbose_name="Геолокация (код с гугл карт)")
    viber = models.CharField(max_length=100, verbose_name="VIBER")
    telegram = models.CharField(max_length=100, verbose_name="TELEGRAM")
    instagram = models.CharField(max_length=100, verbose_name="INSTAGRAM")
    facebook = models.CharField(max_length=100, verbose_name="FACEBOOK")
    telegram_token = models.TextField(verbose_name="Телеграм токен для группы оповещений", null=True,
                                      blank=True)
    tg_chat_id = models.CharField(max_length=100, verbose_name="ИД чата телеграм (для оповещений)", null=True,
                                  blank=True)

    def __str__(self):
        return "Контактные данные ZDRAVO"

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = "Контакты"


class Clients(models.Model):
    phone = models.CharField(max_length=100, verbose_name="Телефон")
    mail = models.CharField(max_length=100, verbose_name="Эл. Почта", null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    comment = models.TextField(verbose_name="Комментарий", null=True, blank=True)

    def __str__(self):
        return self.name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Клиенты'
        verbose_name_plural = "Клиенты"


class ContactForm(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.PROTECT, verbose_name="Клиент", null=True, blank=True)
    comment = models.TextField(verbose_name="Комментарий", null=True, blank=True)
    status = models.CharField(max_length=50, choices=enums.OrderStatus.choices,
                              default=enums.OrderStatus.NEW, verbose_name="Статус")
    date_created = models.DateField(verbose_name="Дата отправки", null=True, blank=True)

    def __str__(self):
        return self.client.name + " " + self.client.last_name + " " + self.client.phone

    class Meta:
        verbose_name = 'Заявки (Контакты)'
        verbose_name_plural = "Заявки (Контакты)"


class CheckUPForm(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.PROTECT, verbose_name="Клиент", null=True, blank=True)
    comment = models.TextField(verbose_name="Комментарий", null=True, blank=True)
    status = models.CharField(max_length=50, choices=enums.OrderStatus.choices,
                              default=enums.OrderStatus.NEW, verbose_name="Статус")
    date_created = models.DateField(verbose_name="Дата отправки", null=True, blank=True)

    def __str__(self):
        return self.client.name + " " + self.client.last_name + " " + self.client.phone

    class Meta:
        verbose_name = 'Заявки (Check-UP)'
        verbose_name_plural = "Заявки (Check-UP)"


class Services(models.Model):
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="service_departament",
                                   verbose_name="Выберите отделение", null=True, blank=True)
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    service_type = models.CharField(max_length=50, choices=enums.ServiceType.choices,
                                    default=enums.ServiceType.CONSULT, verbose_name="Тип Услуги")
    content = QuillField(verbose_name="Описание", null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Цена услуги", default=0)
    slug = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.title).lower().replace(' ', '-'))
        super(Services, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = "Услуги"


class AnalysisCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.title).lower().replace(' ', '-'))
        super(AnalysisCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Анализы (Категории)'
        verbose_name_plural = "Анализы (Категории)"


class AnalysisSubCategory(models.Model):
    parent = models.ForeignKey('AnalysisCategory', on_delete=models.CASCADE, related_name='parent_analysis_category',
                               null=True, blank=True, verbose_name='Категория')
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.title).lower().replace(' ', '-'))
        super(AnalysisSubCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Анализы (Подкатегории)'
        verbose_name_plural = "Анализы (Подкатегории)"


class Analysis(models.Model):
    category = models.ForeignKey(AnalysisCategory, on_delete=models.CASCADE, related_name='analysis_category',
                                 verbose_name='Категория', help_text="Выбирается в случае когда нет подкатегории",
                                 null=True, blank=True)
    subcategory = models.ForeignKey(AnalysisSubCategory, on_delete=models.CASCADE, related_name='analysis_subcategory',
                                    verbose_name='Подкатегория', help_text="Выбирается по умолчанию", null=True,
                                    blank=True)
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Цена услуги", default=0)

    def __str__(self):
        return self.title

    def clean(self):
        if not self.category and not self.subcategory:
            raise ValidationError("Выберите категорию или подкатегорию")

    class Meta:
        verbose_name = 'Анализы'
        verbose_name_plural = "Анализы"


class ServicesInfo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Контент", null=True, blank=True)
    image = models.FileField(upload_to='site_media', verbose_name="Изображение")

    def __str__(self):
        return "Услуги информация"

    class Meta:
        verbose_name = 'Услуги Информация'
        verbose_name_plural = "Услуги Информация"


class ServiceForm(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.PROTECT, verbose_name="Клиент", null=True, blank=True)
    service = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name="Услуга", null=True, blank=True)
    service_type = models.CharField(max_length=50, choices=enums.ServiceType.choices,
                                    default=enums.ServiceType.CONSULT, verbose_name="Тип Услуги")
    comment = models.TextField(verbose_name="Комментарий", null=True, blank=True)
    status = models.CharField(max_length=50, choices=enums.OrderStatus.choices,
                              default=enums.OrderStatus.NEW, verbose_name="Статус")
    date_created = models.DateField(verbose_name="Дата отправки", null=True, blank=True)

    def __str__(self):
        return self.client.name + " " + self.client.last_name + " " + self.client.phone

    class Meta:
        verbose_name = 'Заявки (Онлайн записи)'
        verbose_name_plural = "Заявки (Онлайн записи)"
