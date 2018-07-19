from .models import Ciudad
from rest_framework.serializers import ModelSerializer


class PostCiudad(ModelSerializer):

    class Meta:
        model = Ciudad
        fields = [
            'title',
            'content',
            'lat',
            'lon',
            'user',

        ]