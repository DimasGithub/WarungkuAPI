from django.shortcuts import render
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from deposit.models import Deposit
from warung.models import BioToko, Category, good
from deposit.serializers import DepositSerializer
from warung.serializers import BioSerializer, CategorySerializer, GoodsSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

@api_view(['GET', 'POST'])
def DepositViews(request):
    query = Deposit.objects.all()
    if request.method == 'GET':
        querySerializer = DepositSerializer(query, many=True)
        return JsonResponse(querySerializer.data, safe=False)
    elif request.method == 'POST':
        querySerializer = DepositSerializer(data=request.data)
        if querySerializer.is_valid():
            querySerializer.save()
            return JsonResponse(querySerializer.data, safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(querySerializer.errors, status = status.HTTP_404_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def DepositDetailViews(request, id):
    query = Deposit.objects.get(id=id)
    query2 = Deposit.objects.filter(id=id)
    if request.method == 'GET':
        querySerializer = DepositSerializer(query2, many=True)
        return JsonResponse(querySerializer.data, safe=False)
    elif request.method == 'PUT':
        querySerializer = DepositSerializer(query, data=request.data)
        if querySerializer.is_valid():
            querySerializer.save()
            return JsonResponse(querySerializer.data, safe=False)
        return JsonResponse(querySerializer.errors, status=status.HTTP_404_BAD_REQUEST)
    elif request.method == 'DELETE':
        query.delete()
        serializer_data = DepositSerializer(Deposit.objects.all(), many=True)
        return JsonResponse(serializer_data.data, safe=False)