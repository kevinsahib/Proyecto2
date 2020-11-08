from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView


# --------------MODELOS-------------------
from Profile.models import ProfileModel

# -----------SERIALIZERS--------------------
from Profile.serializers import ProfileModelSerializers

# -------------------VIEWS-----------------
class ProfileModelView(APIView):

    def post(self, request, format=None):
        serializer =  ProfileModelSerializers(data = request.data, context = {'request': request})
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response("Error formato")
