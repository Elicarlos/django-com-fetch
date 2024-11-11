from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from . views import ClienteVieSet, ProdutoViewSet


router = DefaultRouter()
router.register(r'clientes', ClienteVieSet, basename="clientes")
router.register(r'produtos', ProdutoViewSet, basename="produtos")


urlpatterns = [
    path('', views.home, name='home'),
    path('produto/', views.produto, name="produto"),
    path('',include(router.urls))
  
]