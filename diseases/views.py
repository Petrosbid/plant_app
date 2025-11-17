from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Disease
from .serializers import DiseaseSerializer
from .ml_models import predict_disease


class DiseaseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only API endpoint for diseases.
    """
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    permission_classes = [AllowAny]


class DiseaseDiagnoseView(APIView):
    """
    API view for diagnosing a plant disease from an uploaded image.
    """
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        if 'image' not in request.data:
            return Response({'error': 'Image file not provided.'}, status=status.HTTP_400_BAD_REQUEST)

        image_file = request.data['image']

        # Call the stub ML model
        prediction_result = predict_disease(image_file)
        disease_id = prediction_result.get('id')

        if disease_id is None:
            return Response({'error': 'Could not diagnose the disease.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            disease = Disease.objects.get(id=disease_id)
            serializer = DiseaseSerializer(disease)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Disease.DoesNotExist:
            return Response({'error': f'Disease with ID {disease_id} not found in the database.'}, status=status.HTTP_404_NOT_FOUND)