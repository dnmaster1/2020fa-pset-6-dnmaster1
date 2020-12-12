from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet, ViewSet

from .models import DimDate, FactReview
from .serializers import ByYearSerializer, DateSerializer, FactSerializer

class DateViewSet(ModelViewSet):
    queryset = DimDate.objects.all()
    serializer_class = DateSerializer

class FactViewSet(ModelViewSet):
    queryset = FactReview.objects.all()
    serializer_class = FactSerializera
