from django.contrib import admin
from .models import Ciudad

# Register your models here.


class CiudadesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'lat', 'lon')


admin.site.register(Ciudad, CiudadesAdmin)