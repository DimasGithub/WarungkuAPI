from django.db.models import fields
from rest_framework import serializers
from warung.models import BioToko, Category, good

class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = BioToko
        fields = '__all__'

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = good
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    dataku = GoodsSerializer(many=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'dataku']

