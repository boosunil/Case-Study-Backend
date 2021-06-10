from rest_framework import serializers
from .models import Category
import pandas as pd
from django.db import transaction, models


class ImportDataSeializer(serializers.Serializer):
    datafile = serializers.FileField()

    def parse_user_datafile(self, datafile):
        data = []
        df = pd.read_excel(datafile)
        fields = df.columns.to_list()

        df = df.fillna(0)
        for d in df.to_dict(orient='record'):
            data.append(d)
        return data

    @transaction.atomic
    def create(self, validated_data):
        Category.objects.all().delete()
        objs = self.parse_user_datafile(validated_data.get('datafile'))
        for ob in objs:
            obj = Category.objects.create(**ob)
        return objs


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
