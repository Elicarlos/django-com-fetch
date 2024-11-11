from rest_framework import viewsets
from .models import Cliente, Produto
from . serializers import ClienteSerializer, ProdutoSerializer
from django.shortcuts import render

def home(request):
    return render(request, 'core/index.html')

def produto(request):
    return render(request, 'core/produto.html')

class ClienteVieSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer