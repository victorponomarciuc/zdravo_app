from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from multiprocessing import Process

from main.utils.checkUp_form_save import check_up_form_save
from main.utils.contacts_form_save import contact_form_save
from main.models import *
from main.serializers import *
from main.utils.enums import *
from main.utils.online_service_register import service_online_form_save, reg_online_simple


class HomePage(View):
    def get(self, request, *args, **kwargs):
        avantages = AvantagesSection.objects.all().order_by('display_order')
        section_about_clinic = AboutSection.objects.last()
        services = Department.objects.all()
        personal = MedicalPersonal.objects.exclude(category_steep__in=['medsestra', 'sanitar']).order_by('-experience')
        checkup_info = CheckUp.objects.last()
        checkup_items = CheckUpItems.objects.all().order_by('display_order')[:7]
        contacts = ContactsInformation.objects.last()
        departments = Department.objects.all()
        return render(request,
                      template_name='site_app/home_page.html',
                      context={
                          'avantages': avantages,
                          'about_clinic': section_about_clinic,
                          'services': services,
                          'personal_all': personal,
                          'checkup_info': checkup_info,
                          'checkup_items': checkup_items,
                          'contacts': contacts,
                          'departments': departments,
                      })


class CheckUpPage(View):
    def get(self, request, *args, **kwargs):
        page_item = CheckUpItems.objects.get(slug=kwargs['slug'])
        checkup_info = CheckUp.objects.last()
        checkup_items = CheckUpItems.objects.all().order_by('display_order')[:7]
        contacts = ContactsInformation.objects.last()
        departments = Department.objects.all()
        return render(request,
                      template_name='site_app/CheckUp_page.html',
                      context={
                          'checkup_info': checkup_info,
                          'checkup_items': checkup_items,
                          'page_item': page_item,
                          'contacts': contacts,
                          'departments': departments,
                      })


class ServicesVIEW(View):
    def get(self, request, *args, **kwargs):
        contacts = ContactsInformation.objects.last()
        header_content = ServicesInfo.objects.last()
        services = Department.objects.all()
        departments = Department.objects.all()
        return render(request,
                      template_name='site_app/Services.html',
                      context={
                          'contacts': contacts,
                          'header_content': header_content,
                          'services': services,
                          'departments': departments,
                      })


class DepartmentVIEW(View):
    def get(self, request, *args, **kwargs):
        contacts = ContactsInformation.objects.last()
        header_content = ServicesInfo.objects.last()
        department = Department.objects.get(slug=kwargs['slug'])
        consultations = Services.objects.filter(department=department, service_type=enums.ServiceType.CONSULT)
        diagnostics = Services.objects.filter(department=department, service_type=enums.ServiceType.DIAGNOSTIC)
        services = Services.objects.filter(department=department, service_type=enums.ServiceType.SERVICE)
        analysis = Services.objects.filter(department=department, service_type=enums.ServiceType.ANALISIS)
        departments = Department.objects.all()
        return render(request,
                      template_name='site_app/Department.html',
                      context={
                          'contacts': contacts,
                          'header_content': header_content,
                          'department': department,
                          'services': services,
                          'consultations': consultations,
                          'diagnostics': diagnostics,
                          'analysis': analysis,
                          'departments': departments,
                      })


class ProductItemVIEW(View):
    def get(self, request, *args, **kwargs):
        contacts = ContactsInformation.objects.last()
        header_content = ServicesInfo.objects.last()
        product = Services.objects.get(slug=kwargs['slug'])
        departments = Department.objects.all()
        return render(request,
                      template_name='site_app/service_page.html',
                      context={
                          'contacts': contacts,
                          'header_content': header_content,
                          'product': product,
                          'departments': departments,
                      })


class AnalysisView(View):
    def get(self, request, *args, **kwargs):
        categories = AnalysisSubCategory.objects.all
        categories_parent = AnalysisCategory.objects.all()
        analysis = Analysis.objects.all()
        return render(request,
                      template_name='analysis_page.html',
                      context={
                          'categories': categories,
                          'categories_parent': categories_parent,
                          'analysis': analysis,
                      })


class ContactsFormAPI(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'head']

    def list(self, request, *args, **kwargs):
        response = self.serializer_class(instance=self.queryset, many=True).data
        return Response(response, status=200)

    def create(self, request, *args, **kwargs):
        contact_form_save(request.POST)
        return Response('Успіх', status=200)


class CheckUPFormAPI(viewsets.ModelViewSet):
    queryset = CheckUPForm.objects.all()
    serializer_class = CheckUpSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'head']

    def list(self, request, *args, **kwargs):
        response = self.serializer_class(instance=self.queryset, many=True).data
        return Response(response, status=200)

    def create(self, request, *args, **kwargs):
        check_up_form_save(request.POST)
        return Response('Успіх', status=200)


class ServiceFormAPI(viewsets.ModelViewSet):
    queryset = ServiceForm.objects.all()
    serializer_class = ServiceFormSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'head']

    def list(self, request, *args, **kwargs):
        response = self.serializer_class(instance=self.queryset, many=True).data
        return Response(response, status=200)

    def create(self, request, *args, **kwargs):
        reg_online_simple(request.POST)
        return Response('Успіх', status=200)


class ClientsAPI(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    http_method_names = ['get', 'post', 'head']

    def list(self, request, *args, **kwargs):
        clients = Clients.objects.all()
        clients_response = self.serializer_class(instance=clients, many=True).data
        return Response(clients_response, status=200)


class ServicesAPI(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'head']

    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        departament_id = request.GET.getlist('department', None)
        product_id = request.GET.get('service_id', None)
        if departament_id:
            queryset = queryset.filter(department_id__in=departament_id)
        if product_id:
            queryset = Services.objects.filter(pk=product_id)
        services_response = self.serializer_class(instance=queryset, many=True).data
        return Response(services_response, status=200)


def custom_page_not_found_view(request, exception):
    return render(request, "404.html", {})
