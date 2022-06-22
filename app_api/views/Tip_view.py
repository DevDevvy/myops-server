from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.models.tip import Tip
from app_api.models.user import MyOpsUser
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from app_api.models.favorite import Favorite

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
        serializer.save(user=request.auth.user.id)
    
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # list handles queries
    def list(self, request):
        """Handle GET requests to get all tips

        Returns:
            Response -- JSON serialized list of tips
        """
        
        # check if string is a query ie /tip?mood=1
        tip = Tip.objects.all()
        user = request.auth.user
        current_user = MyOpsUser.objects.get(user=user)
        mood = request.query_params.get('mood', None)
        user_id = request.query_params.get('user_id', None)
        if mood is not None:
            tip = tip.filter(mood_id=mood)
        elif user_id is not None:
            tip = tip.filter(user_id=current_user.user_id)
        
        serializer = TipSerializer(tip, many=True)
        return Response(serializer.data)
    
    # added validation 
    def update(self, request, pk):
        """Handle PUT requests for a tip

        Returns:
            Response -- Empty body with 204 status code
        """
        user=MyOpsUser.objects.get(user=request.auth.user)
        tip = Tip.objects.get(pk=pk)
        serializer = CreateTipSerializer(tip, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user.user_id)
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        tip = Tip.objects.get(pk=pk)
        tip.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
    @action(methods=['POST'], detail=True)
    def favorite(self, request, pk):
        """Favorite a tip"""
        try:
            user=request.auth.user
            myops_user = MyOpsUser.objects.get(user=user)
            tip = Tip.objects.get(pk=pk)
            favorite = Favorite.objects.create(
                user_id=myops_user.id,
                tip=tip
            )
            favorite.save()
            return Response({'message': 'Tip Favorited'}, status=status.HTTP_201_CREATED)
        except Tip.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['DELETE'], detail=True)
    def unfavorite(self, request, pk):
        """Unavorite a tip"""
        user=request.auth.user
        myops_user = MyOpsUser.objects.get(user=user)
        favorite = Favorite.objects.get(tip_id=pk, user=myops_user)
        favorite.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class TipSerializer(serializers.ModelSerializer):
    """JSON serializer for tip types
    """
    
    class Meta:
        model = Tip
        fields = ('id', 'tip', 'mood', 'user_id', 'public')
        depth = 1

# validates and saves new tip
class CreateTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = ['tip', 'mood', 'public']