from rest_framework.serializers import ModelSerializer

from .models import DimDate, FactReview

class DateSerializer(ModelSerializer):
    class Meta:
        model = DimDate
        fields = ('date',)

class FactSerializer(ModelSerializer):
    date = DateSerializer(read_only=True)
    class Meta:
        model = FactReview
        fields = ('date','count','useful','stars','funny','cool')





