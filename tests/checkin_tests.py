from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from app_api.models.checkin import CheckIn

from app_api.models.user import MyOpsUser
from app_api.views.Checkin_view import CreateCheckInSerializer


class CheckInTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['users', 'tokens', 'myops_users', 'moods']
    
    def setUp(self):
        # Grab the first Checkin object from the database and add their token to the headers
        self.user = MyOpsUser.objects.first()
        token = Token.objects.get(user=self.user.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_create_checkin(self):
        """Create checkin test"""
        url = "/checkin"

        # Define the Checkin properties
        checkin = {
            "mood_score": 3,
            "self_talk": 6,
            "sleep_quality": 8,
            "coping_strategies": 3,
            "productivity": 1,
            "work_time": 8.0,
            "break_time": 1.0,
            "sleep_time": 6.0,
            "personal_time": 3.0,
            "learning_time": 1.0,
            "exercise_time": 0.0,
        }

        response = self.client.post(url, checkin, format='json')
        
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        
        # Get the last checkin added to the database
        new_checkin = CheckIn.objects.last()

        # Since the create method should return the serialized version of the newly created checkin,
        # Use the serializer you're using in the create method to serialize the "new_checkin"
        expected = CreateCheckInSerializer(new_checkin)

        # Now we can test that output matches what was returned
        self.assertEqual(expected.data, response.data)