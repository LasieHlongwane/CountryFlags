from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Country  # only if you store countries locally

class CountryAPITests(APITestCase):

    def test_country_list_endpoint(self):
        """
        Ensure the /api/countries/ endpoint returns a 200 response.
        """
        url = reverse('country-list')  # make sure your URL name matches
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_country_list_response_format(self):
        """
        Test that response contains a list of countries with expected fields.
        """
        url = reverse('country-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)

        if response.data:
            country = response.data[0]
            self.assertIn('name'),

