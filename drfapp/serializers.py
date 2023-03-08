from rest_framework import serializers
from .models import Linkedin

class LinkedinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Linkedin
        fields = (
            'clientId','code','redirectUri'
        )