from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'clients', ClientsAPI, basename='clients')
router.register(r'contact-form', ContactsFormAPI, basename='contact-form')
router.register(r'check-up-form', CheckUPFormAPI, basename='check-up-form')
router.register(r'online-service-register', ServiceFormAPI, basename='online-service-register')
router.register(r'services', ServicesAPI, basename='services')

urlpatterns = router.urls
