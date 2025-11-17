from rest_framework import serializers
from .models import UserPlant
from plants.serializers import PlantSerializer

class UserPlantSerializer(serializers.ModelSerializer):
    """Serializer for the UserPlant (My Garden) model."""
    plant_details = PlantSerializer(source='plant', read_only=True)

    class Meta:
        model = UserPlant
        fields = ('id', 'user', 'plant', 'plant_details', 'nickname', 'added_date')
        extra_kwargs = {
            'user': {'read_only': True},
            'plant': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
