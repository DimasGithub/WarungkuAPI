from django.db.models import fields
from rest_framework import serializers
from warung.models import BioToko, Stocker, Category, Goods, Deposit

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
class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'