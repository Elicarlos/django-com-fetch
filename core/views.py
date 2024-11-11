from rest_framework import viewsets
from .models import Cliente
from . serializers import ClienteSerializer
from django.shortcuts import render

def home(request):
    return render(request, 'core/index.html')

class ClienteVieSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer