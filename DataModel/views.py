# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Field
from .serializers import FieldSerializer


class FieldListCreateView(generics.ListCreateAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer



class FieldRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer

