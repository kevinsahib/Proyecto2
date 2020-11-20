
from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView


# --------------MODELOS-------------------
from auth_user.models import auth_userModel

# -----------SERIALIZERS--------------------
from auth_user.serializers import auth_userModelSerializers

# -------------------VIEWS-----------------
class auth_userModelView(APIView):

    def post(self, request, format=None):
        serializer =  auth_userModelSerializers(data = request.data, context = {'request': request})
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response("Error formato")
