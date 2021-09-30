from rest_framework import serializers
from warung.models import BioToko, Stocker, Category, Goods

class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = BioToko
        fields = '__all__'
class StockerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Stocker
        fields= '__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'