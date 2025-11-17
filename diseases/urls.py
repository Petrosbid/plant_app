from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DiseaseViewSet, DiseaseDiagnoseView

router = DefaultRouter()
router.register(r'', DiseaseViewSet, basename='disease')

urlpatterns = [
    path('', include(router.urls)),
    path('diagnose/', DiseaseDiagnoseView.as_view(), name='disease-diagnose'),
]
