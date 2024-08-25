from rest_framework import serializers
from fotos.models import Fotos

class FotoSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required = False)
    class Meta:
        model = Fotos
        fields = ('id', 'name', 'autor', 'image')