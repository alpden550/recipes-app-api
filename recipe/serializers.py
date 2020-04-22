from rest_framework import serializers

from api.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """Serializer for a Tag object"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)