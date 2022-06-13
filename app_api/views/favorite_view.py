from rest_framework import serializers
from app_api.models.favorite import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    """JSON serializer for favorites
    """
    class Meta:
        model = Favorite
        fields = ('id', 'tip_id', 'user_id')
        depth=1