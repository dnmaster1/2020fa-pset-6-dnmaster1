from rest_framework.serializers import ModelSerializer

from .models import DimDate, FactReview

class FactSerializer(ModelSerializer):
    class Meta:
        model = FactReview
        fields = ('date','count','stars','useful','funny','cool')


class DateSerializer(ModelSerializer):
    class Meta:
        model = DimDate
        fields = ('date',)