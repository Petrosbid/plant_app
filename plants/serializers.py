from rest_framework import serializers
from .models import Plant

class PlantSerializer(serializers.ModelSerializer):
    """Read-only serializer for the Plant model."""
    class Meta:
        model = Plant
        fields = '__all__'
