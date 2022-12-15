from rest_framework import serializers
from .models import AOT,Titan

class AOTSerializer(serializers.ModelSerializer):
    class Meta:
        model = AOT
        fields = '__all__'

class TitanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titan
        fields = '__all__'
