from rest_framework import serializers
from .models import Country

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name', 'flag']

class CountryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name', 'population', 'capital', 'flag']
