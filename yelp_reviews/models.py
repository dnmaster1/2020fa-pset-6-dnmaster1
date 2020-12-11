from django.db import models

# Create your models here.
from django.db.models import Model


class DimDate(models.Model):
    date = models.DateField(unique=True) # Date field


class FactReview(Model):
    date = models.ForeignKey(DimDate,on_delete=models.CASCADE,unique=True)# ForeignKey
    count = models.IntegerField(default=0) # Integer field; number of reviews on that date
    stars = models.IntegerField(default=0)# Integer, sum of review.stars for all reviews on that date
    useful = models.CharField(max_length=100)
    funny = models.IntegerField(default=0)
    cool = models.BooleanField(max_length=1)
