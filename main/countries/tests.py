from django.test import TestCase
from django.urls import reverse

class CountryAPITests(TestCase):
    
    def test_country_list_response_format(self):
        # Make a GET request to the country list endpoint
        response = self.client.get(reverse('country-list'))
        
        # Assert that the response status is 200 OK
        self.assertEqual(response.status_code, 200)
        
        # If the response contains data, check for the expected keys
        if response.data:
            country = response.data[0]  # Get the first country in the response
            
            # Check if 'name' and 'flag' exist in the country dictionary
            self.assertIn('name', country)
            self.assertIn('flag', country)
            # You can add additional checks for other fields here if needed



