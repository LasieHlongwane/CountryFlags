from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Mock data
COUNTRIES = [
    {"name": "France", "flag": "🇫🇷"},
    {"name": "Japan", "flag": "🇯🇵"},
    {"name": "Brazil", "flag": "🇧🇷"},
]

COUNTRY_DETAILS = {
    "France": {"name": "France", "population": 67000000, "capital": "Paris", "flag": "🇫🇷"},
    "Japan": {"name": "Japan", "population": 125800000, "capital": "Tokyo", "flag": "🇯🇵"},
    "Brazil": {"name": "Brazil", "population": 213000000, "capital": "Brasília", "flag": "🇧🇷"},
}

class CountryListView(APIView):
    def get(self, request):
        return Response(COUNTRIES)

class CountryDetailView(APIView):
    def get(self, request, name):
        country = COUNTRY_DETAILS.get(name)
        if not country:
            return Response({"error": "Country not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(country)

