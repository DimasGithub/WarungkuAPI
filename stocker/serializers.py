from django.db.models import fields
from rest_framework import serializers
from stocker.models import Stocker

class StockerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Stocker
        fields= '__all__'