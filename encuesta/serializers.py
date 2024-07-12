from rest_framework import serializers
from .models import Pais, Nacionalidad, CapituloII, Moneda

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['id', 'nombre', 'codigo']

class NacionalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nacionalidad
        fields = ['id', 'nombre']

class CapituloIISerializer(serializers.ModelSerializer):
    class Meta:
        model = CapituloII
        fields = '__all__'

class MonedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moneda
        fields = ['id', 'nombre', 'codigo_divisa']