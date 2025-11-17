from django.db import models

class Plant(models.Model):
    """Represents a plant in the main database."""
    farsi_name = models.CharField(max_length=255, unique=True)
    scientific_name = models.CharField(max_length=255, unique=True, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='plant_images/', blank=True, null=True)
    is_toxic = models.BooleanField(default=False)
    care_guide = models.JSONField(default=dict)

    def __str__(self):
        return self.farsi_name