from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from app_api.models.checkin import CheckIn

from app_api.models.user import MyOpsUser
from app_api.views.Checkin_view import CheckInSerializer, CreateCheckInSerializer


class CheckInTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['users', 'tokens', 'myops_users', 'moods']
    
    def setUp(self):
        # Grab the first Checkinr object from the database and add their token to the headers
        self.user = MyOpsUser.objects.first()
        token = Token.objects.get(user=self.user.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_create_checkin(self):
        """Create checkin test"""
        url = "/checkin"

        # Define the Checkin properties
        # The keys should match what the create method is expecting
        # Make sure this matches the code you have
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

        # The _expected_ output should come first when using an assertion with 2 arguments
        # The _actual_ output will be the second argument
        # We _expect_ the status to be status.HTTP_201_CREATED and it _actually_ was response.status_code
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        
        # Get the last checkin added to the database, it should be the one just created
        new_checkin = CheckIn.objects.last()

        # Since the create method should return the serialized version of the newly created checkin,
        # Use the serializer you're using in the create method to serialize the "new_checkin"
        # Depending on your code this might be different
        expected = CreateCheckInSerializer(new_checkin)

        # Now we can test that the expected ouput matches what was actually returned
        self.assertEqual(expected.data, response.data)