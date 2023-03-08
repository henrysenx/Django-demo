from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from drfapp.serializers import LinkedinSerializer
from drfapp.models import Linkedin

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "username":"Admin",
            "no_of_years_active":10
        }
        return Response(data)
    
    def post(self, request, *args, **kwargs):
        # serializer = LinkedinSerializer(data=request.data)
        # if(serializer.is_valid):
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors)
        return Response(data=request.data)