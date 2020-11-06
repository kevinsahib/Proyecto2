from rest_framework import serializers

from Profile.models import ProfileModel

class  ProfileModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fileds = ('__all__')
