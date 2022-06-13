from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.models.journal import Journal
from app_api.models.user import MyOpsUser
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from app_api.models.favorite import Favorite

class JournalView(ViewSet):
    """Journals view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single journal

        Returns:
            Response -- JSON serialized journal
        """
        try:
            journal = Journal.objects.get(pk=pk)
            serializer = JournalSerializer(journal)
            return Response(serializer.data)
        except Journal.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    # create a new journal
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """
        user = MyOpsUser.objects.get(user=request.auth.user)
        serializer = CreateJournalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
    
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # list handles queries
    def list(self, request):
        """Handle GET requests to get all journals

        Returns:
            Response -- JSON serialized list of journals
        """
        
        # check if string is a query ie /journal?mood=1
        current_user = MyOpsUser.objects.get(user=request.auth.user)
        journal = Journal.objects.filter(user=current_user)
        mood = request.query_params.get('mood', None)
        
        if mood is not None:
            journal = journal.filter(mood_id=mood)
        
        serializer = JournalSerializer(journal, many=True)
        return Response(serializer.data)
    
    # added validation 
    def update(self, request, pk):
        """Handle PUT requests for a journal

        Returns:
            Response -- Empty body with 204 status code
        """
        user=MyOpsUser.objects.get(user=request.auth.user)
        journal = Journal.objects.get(pk=pk)
        serializer = CreateJournalSerializer(journal, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        journal = Journal.objects.get(pk=pk)
        journal.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)



class JournalSerializer(serializers.ModelSerializer):
    """JSON serializer for journal types
    """
    
    class Meta:
        model = Journal
        fields = ('id', 'content', 'date', 'mood', 'user', 'title')
        depth = 1

# validates and saves new journal
class CreateJournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['content', 'mood', 'title']