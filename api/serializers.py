from rest_framework import serializers
from .models import Field
from django.core.validators import MinValueValidator, MaxValueValidator

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ['First_Name', 'Middle_Name', 'Last_Name', 'Email', 'Phone_Number', 'Service_Type', 'Location', 'details', 'terms1', 'terms2', 'terms3']
