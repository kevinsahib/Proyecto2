from rest_framework import serializers

from Alumnos.models import AlumnosModel

class  AlumnosModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = AlumnosModel
        fields = ('__all__')