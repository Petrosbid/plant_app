from django.db import models

class Disease(models.Model):
    """Represents a plant disease in the main database."""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    symptoms = models.TextField()
    solution = models.TextField()
    affected_plants = models.ManyToManyField('plants.Plant', related_name='diseases', blank=True)

    def __str__(self):
        return self.name