from django.db import models
from django.contrib.auth import settings

# Create your models here.

class Ciudad(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = models.TextField(verbose_name="Descripción")
    lat = models.DecimalField(verbose_name="Latitud", default=0, max_digits=20, decimal_places=6)
    lon = models.DecimalField(verbose_name="Longitud", default=0, max_digits=20, decimal_places=6)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=999, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        ordering = ['-title']

    def __str__(self):
        return self.title
