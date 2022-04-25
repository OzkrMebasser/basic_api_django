from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from base.models import Tour
from base.models import User

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
