from django.shortcuts import render
from debt.models import Debt
from debt.serializers import DebtSerializer
from django.shortcuts import render
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from warung import serializers
from warung.models import BioToko, Category, good
from warung.serializers import BioSerializer, CategorySerializer, GoodsSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

@api_view(['GET', 'POST'])
def DebtViews(request):
    query = Debt.objects.all()
    if request.method == 'GET':
        querySerializer = DebtSerializer(query, many=True)
        return JsonResponse(querySerializer.data, safe=False)
    elif request.method == 'POST':
        querySerializer = DebtSerializer(data=request.data)
        if querySerializer.is_valid():
            querySerializer.save()
            return JsonResponse(querySerializer.data, safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(querySerializer.errors, status = status.HTTP_404_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def DebtDetailViews(request, id):
    query = Debt.objects.get(id=id)
    query2 = Debt.objects.filter(id=id)
    if request.method == 'GET':
        querySerializer = DebtSerializer(query2, many=True)
        return JsonResponse(querySerializer.data, safe=False)
    elif request.method == 'PUT':
        querySerializer = DebtSerializer(query, data=request.data)
        if querySerializer.is_valid():
            querySerializer.save()
            return JsonResponse(querySerializer.data, safe=False)
        return JsonResponse(querySerializer.errors, status=status.HTTP_404_BAD_REQUEST)
    elif request.method == 'DELETE':
        query.delete()
        serializer_data = DebtSerializer(Debt.objects.all(), many=True)
        return JsonResponse(serializer_data.data, safe=False)
# Create your views here.
