from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=255)
    api_id = models.PositiveIntegerField(unique=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    origin_name = models.CharField(max_length=255, blank=True, null=True)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} (#{self.api_id})"
