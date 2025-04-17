from django.urls import path
from .views import CountryListView, CountryDetailView

urlpatterns = [
    path('countries/', CountryListView.as_view(), name='country-list'),
    path('countries/<str:name>/', CountryDetailView.as_view(), name='country-detail'),
    path('countries/', CountryListView.as_view(), name='country-list'),

]



