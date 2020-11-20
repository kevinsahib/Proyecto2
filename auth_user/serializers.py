from rest_framework import serializers

from auth_user.models import auth_userModel

class  auth_userModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = auth_userModel
        fields = ('__all__')