from rest_framework import serializers
from mensagem.models import *


class MensageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensagem
        fields = ('id', 'nome', 'texto',)
