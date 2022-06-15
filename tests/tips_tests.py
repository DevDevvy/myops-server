from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from app_api.models.tip import Tip
from app_api.models.user import MyOpsUser
from app_api.views.tip_view import CreateTipSerializer


class TipsTests(APITestCase):

    # Add any fixtures you want to run to build the test database
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
        # The keys should match what the create method is expecting
        # Make sure this matches the code you have
        tip = {
            "tip": "Be sure to drink your ovalteen",
            "mood": 2
        }

        response = self.client.post(url, tip, format='json')

        # The _expected_ output should come first when using an assertion with 2 arguments
        # The _actual_ output will be the second argument
        # We _expect_ the status to be status.HTTP_201_CREATED and it _actually_ was response.status_code
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        
        # Get the last tip added to the database, it should be the one just created
        new_tip = Tip.objects.last()

        # Since the create method should return the serialized version of the newly created tip,
        # Use the serializer you're using in the create method to serialize the "new_tip"
        # Depending on your code this might be different
        expected = CreateTipSerializer(new_tip)

        # Now we can test that the expected ouput matches what was actually returned
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