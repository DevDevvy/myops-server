from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from app_api.models.myops_user import MyOpsUser


class MyOpsUserView(ViewSet):
    """MyOps User view"""
    
    def list(self, request):
        """Handle GET requests to get current user

        Returns:
            Response -- JSON serialized list of game types
        """
        user = MyOpsUser.objects.get(user=request.auth.user)
        serializer = MyOpsUserSerializer(user)
        return Response(serializer.data)


class MyOpsUserSerializer(serializers.ModelSerializer):
    """JSON serializer for game
    """
    class Meta:
        model = MyOpsUser
        fields = ('id', 'user_id', 'user_photo')
        depth = 1
        
