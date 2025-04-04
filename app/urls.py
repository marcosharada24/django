from django.urls import path

from . import views

urlpatterns = [
  path('', views.app, name="index"),
  path('usuarios', views.exibirUsuarios, name="exibirUsuarios"),

  path('add-usuario', views. 
       addUsuario, name="addUsuario")
]