from django.db.models import fields
from rest_framework import serializers
from warung.models import BioToko, Stocker, Category, Goods, Deposit, Sold, Debt

class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = BioToko
        fields = '__all__'

class StockerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Stocker
        fields= '__all__'

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    dataku = GoodsSerializer(many=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'dataku']

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'

class SoldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sold
        fields = '__all__'

class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = '__all__'
