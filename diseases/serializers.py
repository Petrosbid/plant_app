from rest_framework import serializers
from .models import Disease

class DiseaseSerializer(serializers.ModelSerializer):
    """Read-only serializer for the Disease model."""
    class Meta:
        model = Disease
        fields = '__all__'
