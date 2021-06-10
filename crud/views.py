from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContactInfoSerializer
from .models import ContactInfo
from .renderers import CustomRenderer

# Create your views here.


class ContactInfo(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    renderer_classes = (CustomRenderer,)
