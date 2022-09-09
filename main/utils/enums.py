from django.db import models
from django.utils.translation import pgettext_lazy as _


class PersonalCategorySTEP(models.TextChoices):
    TOP = "vishya_categoriya", _('personal category', 'Вища категорія')
    MIDDLE = "serednya_categoriya", _('personal category', 'Середня категорія')
    INTERN = "intern", _('personal category', 'Интерн')
    NURSE = "medsestra", _('personal category', 'Медсестра')
    SANITAR = "sanitar", _('personal category', 'Санитар')
    NOCATEGORY = "no_category", _('personal category', 'Без категоріi')


class OrderStatus(models.TextChoices):
    NEW = "new", _('order category', 'Нова')
    PROCESSING = "processing", _('order category', 'В обробці')
    COMPLETE = "complete", _('order category', 'Завершено')


class ServiceType(models.TextChoices):
    CONSULT = "consult", _('service Type', 'Консультация')
    DIAGNOSTIC = "diagnostic", _('service Type', 'Диангостика')
    SERVICE = "service", _('service Type', 'Услуга')
    ANALISIS = "service_analisys", _('service Type', 'Анализы')
