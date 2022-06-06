from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.models.tip import Tip
from app_api.models.myops_user import MyOpsUser

class TipView(ViewSet):
    """Tips view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single tip

        Returns:
            Response -- JSON serialized tip
        """
        try:
            tip = Tip.objects.get(pk=pk)
            serializer = TipSerializer(tip)
            return Response(serializer.data)
        except Tip.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    # create a new tip
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """
        user = MyOpsUser.objects.get(user=request.auth.user)
        serializer = CreateTipSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
    
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # list handles queries
    def list(self, request):
        """Handle GET requests to get all tips

        Returns:
            Response -- JSON serialized list of tips
        """
        tip = Tip.objects.all()
        # check if string is a query ie /tip?mood=1
        mood = request.query_params.get('mood', None)
        if mood is not None:
            tip = tip.filter(mood_id=mood)
        
        serializer = TipSerializer(tip, many=True)
        return Response(serializer.data)
    
    # added validation 
    def update(self, request, pk):
        """Handle PUT requests for a tip

        Returns:
            Response -- Empty body with 204 status code
        """
        tip = Tip.objects.get(pk=pk)
        serializer = CreateTipSerializer(tip, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        tip = Tip.objects.get(pk=pk)
        tip.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        

class TipSerializer(serializers.ModelSerializer):
    """JSON serializer for tip types
    """
    class Meta:
        model = Tip
        fields = ('id', 'tip', 'mood', 'user')
        depth = 1
        
# validates and saves new tip
class CreateTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = ['tip', 'mood']