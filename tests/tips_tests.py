from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from app_api.models.tip import Tip
from app_api.models.user import MyOpsUser
from app_api.views.Tip_view import CreateTipSerializer


class TipsTests(APITestCase):

    fixtures = ['users', 'tokens', 'myops_users', 'moods', 'tips']
    
    def setUp(self):
        # Grab the first User object from the database and add their token to the headers
        self.user = MyOpsUser.objects.first()
        token = Token.objects.get(user=self.user.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_create_tip(self):
        """Create tip test"""
        url = "/tips"

        # Define the Tip properties
        
        tip = {
            "tip": "Be sure to drink your ovalteen",
            "mood": 2
        }

        response = self.client.post(url, tip, format='json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        
        # Get the last tip added to the database
        new_tip = Tip.objects.last()

        expected = CreateTipSerializer(new_tip)

        self.assertEqual(expected.data, response.data)
        
    def test_delete_tip(self):
        """Test delete tip"""
        tip = Tip.objects.last()
        tipId = tip.id
        url = f'/tips/{tipId}'
        response = self.client.delete(url)

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

        # Test that it was deleted by trying to _get_ the tip
        # The response should return a 404
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)