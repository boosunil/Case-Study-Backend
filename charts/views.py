from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.parsers import \
    (
        MultiPartParser,
        FormParser
    )
from rest_framework.decorators import action
from .models import Category
from .utils import multipart_viewset_parser
from .utils import Response
from .serializers import ImportDataSeializer, CategorySerializer


# Create your views here.

class ImportView(viewsets.ModelViewSet):

    queryset = Category.objects.all()

    @action(methods=['post'],
            detail=False,
            serializer_class=ImportDataSeializer,
            parser_classes=(MultiPartParser, FormParser,),
            url_path="add")
    def import_data(self, request):
        multipart_viewset_parser(request)
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        data = ser.save()
        resp_msg = f'Data has been successfully Imported'
        return Response({resp_msg})

    @action(methods=['get'],
            detail=False,
            serializer_class=CategorySerializer,
            url_path="get")
    def get_data(self, request):
        query_set = Category.objects.all()
        serializer = self.get_serializer(query_set, many=True)
        return Response(serializer.data)
