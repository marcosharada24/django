from django.urls import path

from . import views

urlpatterns = [
  path('', views.app, name="index"),
  path('usuarios', views.exibirUsuarios, name="exibirUsuarios"),

  path('add-usuario', views.addUsuario, name="addUsuario"),

  path('exluir-usuario/<int:id_usuario>', views.excluirUsuario, name="excluirUsuario"),

  path('editar-usuario/<int:id_usuario>', views.editarUsuario, name="editarUsuario"),

  path('cadastrarProduto', views.cadastrarProduto, name="cadastrarProduto"),
]