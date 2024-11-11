from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from . views import ClienteVieSet


router = DefaultRouter()
router.register(r'clientes', ClienteVieSet)


urlpatterns = [
    path('', views.home, name='home'),
    path('',include(router.urls))
  
]