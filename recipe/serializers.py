from rest_framework import serializers

from api.models import Ingredient, Tag


class TagSerializer(serializers.ModelSerializer):
    """Serializer for a Tag object"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for a Ingredient object"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)
