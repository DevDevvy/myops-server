from django.db import models
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

class Tip(models.Model):
    tip = models.CharField(max_length=50)
    mood = models.ForeignKey("Mood", on_delete=models.CASCADE)
    user = models.ForeignKey("MyOpsUser", on_delete=models.CASCADE)
    # write a custom function for users to "favorite" a tip
    
    @action(methods=['POST'], detail=True)
    def favorite(self, request, pk):
        """Favorite a tip"""
        try:
            user=request.auth.user
            tip = Tip.objects.get(pk=pk)
            fave = Favorite.objects.create(
                tip=tip,
                user=user
            )
            fave.save()
            return Response({'message': 'Tip Favorited'}, status=status.HTTP_201_CREATED)
        except Tip.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['DELETE'], detail=True)
    def unfavorite(self, request, pk):
        """Unavorite a tip"""
        user=request.auth.user
        favorite = Favorite.objects.get(tip_id=pk, user=user)
        favorite.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)