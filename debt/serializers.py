from django.db.models import fields
from rest_framework import serializers
from debt.models import Debt
class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = '__all__'
