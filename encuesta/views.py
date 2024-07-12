from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Pais, Nacionalidad, CapituloII, Moneda
from .serializers import PaisSerializer, NacionalidadSerializer, CapituloIISerializer, MonedaSerializer

class PaisViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

class NacionalidadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = NacionalidadSerializer

class CapituloIIViewSet(viewsets.ModelViewSet):
    queryset = CapituloII.objects.all()
    serializer_class = CapituloIISerializer

class MonedaListCreate(generics.ListCreateAPIView):
    queryset = Moneda.objects.all()
    serializer_class = MonedaSerializer

class MonedaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Moneda.objects.all()
    serializer_class = MonedaSerializer
