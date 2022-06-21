from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from app_api.models.user import MyOpsUser
from app_api.views.tip_view import TipSerializer

# gets user logged in at /currentuser
class MyOpsUserView(ViewSet):
    """MyOps User view"""
    
    def list(self, request):
        """Handle GET requests to get current user

        Returns:
            Response -- JSON serialized list of game types
        """
        user =request.auth.user
        current_user = MyOpsUser.objects.get(user_id=user)
        serializer = MyOpsUserSerializer(current_user)
        return Response(serializer.data)


class MyOpsUserSerializer(serializers.ModelSerializer):
    """JSON serializer for user
    """
    favoritedtips = TipSerializer(many=True)
    class Meta:
        model = MyOpsUser
        fields = ('id', 'user_id', 'favoritedtips', 'username', 'first_name', 'last_name', 'bio')
        depth=1

