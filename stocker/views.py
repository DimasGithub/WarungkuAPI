from django.shortcuts import render
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from stocker.models import Stocker
from stocker.serializers import StockerSerializer

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
