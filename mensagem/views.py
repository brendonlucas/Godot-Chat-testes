from rest_framework import status, generics, pagination
from mensagem.serializers import *
from mensagem.models import *



class Mensagem(generics.ListCreateAPIView):
    queryset = Mensagem.objects.all()
    serializer_class = MensageSerializer
