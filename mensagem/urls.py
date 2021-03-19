from django.urls import path

from mensagem.views import *
from mensagem import views

urlpatterns = [
    #path('mensagem/', views.Mensagem, name='Mensagem'),
    path('mensagems/', Mensagem.as_view(), name='list_lojas'),
    # path('lojas/<int:id_loja>/', LojaDetalhes.as_view(), name='Detalhes_lojas'),
]
