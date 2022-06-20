from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.models.checkin import CheckIn
from app_api.models.journal import Journal

from app_api.models.user import MyOpsUser
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from app_api.models.favorite import Favorite

from django.db.models import Subquery, OuterRef

from app_api.views.journal_view import JournalSerializer

class CheckInView(ViewSet):
    """Check-in view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single checkin
        Returns:
            Response -- JSON serialized checkin
        """
        try:
            checkin = CheckIn.objects.get(pk=pk)
            serializer = CheckInSerializer(checkin)
            return Response(serializer.data)
        except CheckIn.DoesNotExist as ex:
            
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    # create a new checkin
    def create(self, request):
        """Handle POST operations for checkin

        Returns:
            Response -- JSON serialized game instance
        """
        user = MyOpsUser.objects.get(user=request.auth.user)
        serializer = CreateCheckInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
    
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # list handles queries
    def list(self, request):
        """Handle GET requests to get all checkins
        Returns:
            Response -- JSON serialized list of checkins
        """
        user = MyOpsUser.objects.get(user=request.auth.user)
        
        days = request.query_params.get('days', None)
        if days is not None:
            checkins = CheckIn.objects.filter(user=user).order_by('-date')[:int(days):-1]
        else:
            checkins = CheckIn.objects.filter(user=user).order_by('-date')[:7:-1]
            for checkin in checkins:
                try:
                    journals = Journal.objects.filter(user=user, date__contains=checkin.date.day)
                    serializer = JournalSerializer(journals, many=True)
                    checkin.journal = serializer.data
                except Journal.DoesNotExist:
                    checkin.journals = None
        serializer = CheckInSerializer(checkins, many=True)
        
        return Response(serializer.data)
    
    # added validation 
    def update(self, request, pk):
        """Handle PUT requests for a checkin
        Returns:
            Response -- Empty body with 204 status code
        """
        checkin = CheckIn.objects.get(pk=pk)
        serializer = CreateCheckInSerializer(checkin, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        checkin = CheckIn.objects.get(pk=pk)
        checkin.delete()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
   


class CheckInSerializer(serializers.ModelSerializer):
    """JSON serializer for checkin types
    """
    class Meta:
        model = CheckIn
        fields = ('id', 'date', 'mood_score', 'self_talk', 'sleep_quality', 'coping_strategies', 'productivity', 'work_time', 'break_time', 'sleep_time', 'personal_time', 'learning_time', 'exercise_time', 'user_id', 'journal')
        depth = 1
        
# validates and saves new checkin
class CreateCheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ['mood_score', 'self_talk', 'sleep_quality', 'coping_strategies', 'productivity', 'work_time', 'break_time', 'sleep_time', 'personal_time', 'learning_time', 'exercise_time']