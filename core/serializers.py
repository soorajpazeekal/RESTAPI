from rest_framework.serializers import ModelSerializer
from core.models import Luggage, Order
from rest_framework import serializers
from django.contrib.auth.models import User

class LuggageSerializer(ModelSerializer):
    class Meta:
        model = Luggage
        fields = '__all__'

    

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__' 