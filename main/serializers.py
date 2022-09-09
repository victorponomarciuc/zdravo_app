from rest_framework import serializers

from main import models


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactForm
        exclude = []


class CheckUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CheckUPForm
        exclude = []


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clients
        exclude = []


class ServiceFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceForm
        exclude = []


class ServicesSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField(read_only=False)

    @staticmethod
    def get_content(instance):
        return str(instance.content.html)

    class Meta:
        model = models.Services
        exclude = []
        fields = ['id', 'title', 'service_type', 'content', 'price']


