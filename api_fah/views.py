from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Alquran
from .serializers import AlquranSerializer

class AlquranViewSet(viewsets.ModelViewSet):
    queryset = Alquran.objects.all().order_by('ayat').order_by('surat')
    serializer_class = AlquranSerializer
    http_method_names = ['get', 'head']
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'surat':['exact'], 
        'ayat':['exact']}