from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlantViewSet, PlantIdentifyView

router = DefaultRouter()
router.register(r'', PlantViewSet, basename='plant')

urlpatterns = [
    path('', include(router.urls)),
    path('identify/', PlantIdentifyView.as_view(), name='plant-identify'),
]
