from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import UserPlant
from .serializers import UserPlantSerializer

class UserPlantViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing a user's personal garden (UserPlant).
    """
    serializer_class = UserPlantSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should only return the list of plants
        for the currently authenticated user.
        """
        return UserPlant.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Automatically associate the user with the new UserPlant instance.
        """
        serializer.save(user=self.request.user)

    def get_serializer_context(self):
        """
        Pass the request context to the serializer.
        """
        return {'request': self.request}