from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from warung import serializers
from warung.models import BioToko, Stocker, Category, Goods, Deposit
from warung.serializers import BioSerializer, StockerSerializer, CategorySerializer, GoodsSerializer, DepositSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def warungView(request):
    if request.method == 'GET':
        data = BioToko.objects.all()
        data_serializer = BioSerializer(data, many=True)
        return JsonResponse(data_serializer.data, safe=False)
    elif request.method == 'POST':
        data_serializer = BioSerializer(data=request.data)
        if data_serializer.is_valid():
            data_serializer.save()
            return JsonResponse(data_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(data_serializer.errors, status=status.HTTP_404_BAD_REQUEST)
    
@api_view(['GET', 'PUT'])
def warungDetail(request, id):
    query = BioToko.objects.get(id=id)
    data = BioToko.objects.filter(id=id)
    if request.method == 'PUT':
        serializer = BioSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data)
    elif request.method == 'GET':
        dataku = BioSerializer(data, many=True)
        return Response(dataku.data)

@api_view(['GET', 'POST'])
def StockerViews(request):
    query = Stocker.objects.all()
    if request.method == 'GET':
        querySerializer = StockerSerializer(query, many=True)
        return JsonResponse(querySerializer.data, safe=False)
    elif request.method == 'POST':
        querySerializer = StockerSerializer(data=request.data)
        if querySerializer.is_valid():
            querySerializer.save()
            return JsonResponse(querySerializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(querySerializer.errors, status=status.HTTP_404_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def StockerDetailViews(request, id):
    query = Stocker.objects.get(id=id)
    query2 = Stocker.objects.filter(id=id)
    if request.method == 'GET':
        querySerializer = StockerSerializer(query2, many=True)
        return JsonResponse(querySerializer.data, safe=False)
    elif request.method == 'PUT':
        querySerializer = StockerSerializer(query, data=request.data)
        if querySerializer.is_valid():
            querySerializer.save()
            return JsonResponse(querySerializer.data, safe=False)
        return JsonResponse(querySerializer.errors, status=status.HTTP_404_BAD_REQUEST)
    elif request.method == 'DELETE':
        query.delete()
        querySerializer = StockerSerializer(query, many=True)
        return JsonResponse(querySerializer.data, safe=False)

@api_view(['GET', 'POST'])
def CategoryViews(request):
    query = Category.objects.all()
    if request.method == 'GET':
        querySerializer = CategorySerializer(query, many=True)
        return JsonResponse(querySerializer.data, safe=False)
    elif request.method == 'POST':
        querySerializer = CategorySerializer(data=request.data)
        if querySerializer.is_valid():
            querySerializer.save()
            return JsonResponse(querySerializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(querySerializer.errors, status=status.HTTP_404_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def CategoryDetailViews(request, id):
    query = Category.objects.get(id=id)
    query2 = Category.objects.filter(id=id)
    if request.method == 'PUT':
        serializer_data = CategorySerializer(query, data= request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return JsonResponse(serializer_data.data)
        return JsonResponse(serializer_data.errors, status=status.HTTP_404_BAD_REQUEST)
    elif request.method == 'DELETE':
        query.delete()
        serializer_data = CategorySerializer(Category.objects.all(), many=True) 
        return JsonResponse(serializer_data.data, safe=False)
    elif request.method == 'GET':
        serializer_data = CategorySerializer(query2, many=True)
        return JsonResponse(serializer_data.data, safe=False)

@api_view(['GET', 'POST'])
def GoodsViews(request):
    query = Goods.objects.all()
    if request.method == 'GET':
        querySerializer = GoodsSerializer(query, many=True)
        return JsonResponse(querySerializer.data, safe=False)
    elif request.method == 'POST':
        querySerializer = GoodsSerializer(data=request.data)
        if querySerializer.is_valid():
            querySerializer.save()
            return JsonResponse(querySerializer.data, safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(querySerializer.errors, status=status.HTTP_404_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def GoodsDetailViews(request, id):
    query = Goods.objects.get(id=id)
    query2 = Goods.objects.filter(id=id)
    if request.method == 'GET':
        querySerializer = GoodsSerializer(query2, many=True)
        return JsonResponse(querySerializer.data, safe=False)
    elif request.method == 'PUT':
        querySerializer = GoodsSerializer(query, data = request.data)
        if querySerializer.is_valid():
            querySerializer.save()
            return JsonResponse(querySerializer.data, safe=False)
    elif request.method == 'DELETE':
        query.delete()
        serializer_data = GoodsSerializer(Goods.objects.all(), many=True)
        return JsonResponse(serializer_data.data, safe=False)

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
