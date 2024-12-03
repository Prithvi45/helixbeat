from __future__ import division
from rest_framework import serializers
from .models import *



class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'
