from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.models.mood import Mood
from app_api.models.tip import Tip
from app_api.models.user import MyOpsUser

class MoodView(ViewSet):
    """Moods view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single mood

        Returns:
            Response -- JSON serialized mood
        """
        try:
            mood = Mood.objects.get(pk=pk)
            serializer = MoodSerializer(mood)
            return Response(serializer.data)
        except Mood.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    # create a new mood
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """
        user = MyOpsUser.objects.get(user=request.auth.user)
        serializer = CreateMoodSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
    
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # list handles queries
    def list(self, request):
        """Handle GET requests to get all moods

        Returns:
            Response -- JSON serialized list of moods
        """
        moods = Mood.objects.all()
        # check if string is a query ie /mood?id=1
        id = request.query_params.get('id', None)
        if id is not None:
            moods = moods.filter(id=id)
        
        serializer = MoodSerializer(moods, many=True)
        return Response(serializer.data)
    

class MoodSerializer(serializers.ModelSerializer):
    """JSON serializer for mood types
    """
    class Meta:
        model = Mood
        fields = ('id', 'mood')
        
# validates and saves new mood
class CreateMoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ['mood']