from django.conf import settings
from django.db import models

class UserPlant(models.Model):
    """Represents a plant in a user's personal garden."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='garden')
    plant = models.ForeignKey('plants.Plant', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'plant')

    def __str__(self):
        return f"{self.nickname or self.plant.farsi_name} in {self.user.username}'s garden"