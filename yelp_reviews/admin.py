from django.contrib import admin

# Register your models here.
from .models import DimDate, FactReview
admin.site.register(DimDate)
admin.site.register(FactReview)
