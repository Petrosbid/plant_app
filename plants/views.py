from rest_framework import viewsets, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Plant
from .serializers import PlantSerializer
from .ml_models import predict_plant


class PlantViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only API endpoint for plants.
    Supports searching by 'farsi_name' and 'scientific_name'.
    """
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['farsi_name', 'scientific_name']


class PlantIdentifyView(APIView):
    """
    API view for identifying a plant from an uploaded image.
    """
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        if 'image' not in request.data:
            return Response({'error': 'Image file not provided.'}, status=status.HTTP_400_BAD_REQUEST)

        image_file = request.data['image']
        
        # Call the stub ML model
        prediction_result = predict_plant(image_file)
        plant_id = prediction_result.get('id')

        if plant_id is None:
            return Response({'error': 'Could not identify the plant.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            plant = Plant.objects.get(id=plant_id)
            serializer = PlantSerializer(plant)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Plant.DoesNotExist:
            return Response({'error': f'Plant with ID {plant_id} not found in the database.'}, status=status.HTTP_404_NOT_FOUND)