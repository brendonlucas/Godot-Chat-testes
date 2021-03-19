from rest_framework import status, generics, pagination
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from mensagem.serializers import *
from rest_framework import filters
from mensagem.models import *
from rest_framework import viewsets


class Mensagem(generics.ListCreateAPIView):
    queryset = Mensagem.objects.all()
    serializer_class = MensageSerializer
