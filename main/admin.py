from main.models import *
import nested_admin
from django.contrib import admin


# Register your models here.

@admin.register(AvantagesSection)
class AvantagesSectionAdmin(nested_admin.NestedModelAdmin):
    extra = 0
    exclude = []


@admin.register(AboutSection)
class AboutSectionAdmin(nested_admin.NestedModelAdmin):
    extra = 0
    exclude = []


@admin.register(Services)
class ServicesAdmin(nested_admin.NestedModelAdmin):
    extra = 0
    exclude = []
    readonly_fields = ['slug']


@admin.register(Department)
class DeparmentAdmin(nested_admin.NestedModelAdmin):
    extra = 0
    exclude = []
    readonly_fields = ['slug']


@admin.register(PersonalPostPosition)
class PersonalPostPositionAdmin(nested_admin.NestedModelAdmin):
    extra = 0
    exclude = []
    readonly_fields = ['slug']


@admin.register(MedicalPersonal)
class MedicalPersonalAdmin(nested_admin.NestedModelAdmin):
    extra = 0
    exclude = []


@admin.register(CheckUp)
class CheckUpAdmin(nested_admin.NestedModelAdmin):
    extra = 0
    exclude = []


@admin.register(CheckUpItems)
class CheckUpItemsAdmin(nested_admin.NestedModelAdmin):
    extra = 0
    exclude = []
    readonly_fields = ['slug']


@admin.register(ContactsInformation)
class ContactsInformationAdmin(nested_admin.NestedModelAdmin):
    extra = 0
    exclude = []


@admin.register(ContactForm)
class ContactFormAdmin(nested_admin.NestedModelAdmin):
    extra = 0
    exclude = []
    list_display = ('id', 'client', 'date_created', 'status')


@admin.register(Clients)
class ClientsAdmin(nested_admin.NestedModelAdmin):
    extra = 0
    exclude = []
    list_display = ('name', 'last_name', 'phone', 'mail')


@admin.register(ServicesInfo)
class ServicesInfoAdmin(nested_admin.NestedModelAdmin):
    extra = 0
    exclude = []


@admin.register(AnalysisCategory)
class AnalysisCategoryAdmin(nested_admin.NestedModelAdmin):
    extra = 0
    exclude = []
    readonly_fields = ['slug']


@admin.register(AnalysisSubCategory)
class AnalysisSubCategoryCategoryAdmin(nested_admin.NestedModelAdmin):
    extra = 0
    exclude = []
    readonly_fields = ['slug']


@admin.register(Analysis)
class AnalysisAdmin(nested_admin.NestedModelAdmin):
    extra = 0
    exclude = []


@admin.register(CheckUPForm)
class CheckUPFormAdmin(nested_admin.NestedModelAdmin):
    extra = 0
    exclude = []
    list_display = ('id', 'client', 'date_created', 'status')


@admin.register(ServiceForm)
class ServiceFormAdmin(nested_admin.NestedModelAdmin):
    extra = 0
    exclude = []
    list_display = ('id', 'client', 'date_created', 'status')
