from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
    path('checkup/<slug>', views.CheckUpPage.as_view(), name='check-up_page'),
    path('departments', views.ServicesVIEW.as_view(), name='departments'),
    path('departmens/<slug>', views.DepartmentVIEW.as_view(), name='department_page'),
    path('service/<slug>', views.ProductItemVIEW.as_view(), name='service_page'),
    path('analysis/', views.AnalysisView.as_view(), name='analysis_page'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'main.views.custom_page_not_found_view'
