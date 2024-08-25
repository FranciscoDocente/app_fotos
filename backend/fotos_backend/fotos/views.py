from django.shortcuts import render
from rest_framework import generics
from fotos.models import Fotos
from fotos.serializer import FotoSerializer
from rest_framework import viewsets

class FotoViewSet(viewsets.ModelViewSet):
    queryset = Fotos.objects.all()
    serializer_class = FotoSerializer

# Create your views here.
""" class FotoListAPiView(generics.ListAPIView):
    queryset = Fotos.objects.all()
    serializer_class = FotoSerializer
    
class FotoDetailAPIView(generics.RetrieveAPIView):
    queryset = Fotos.objects.all()
    serializer_class = FotoSerializer """