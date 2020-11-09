from rest_framework import serializers

import django_filters
from .models import Alquran

class AlquranSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alquran
        fields = ('surat', 'ayat', 'arab', 'indonesia')

class AlquranFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    
    class Meta:
        model = Alquran
        fields = ['surat', 'ayat']