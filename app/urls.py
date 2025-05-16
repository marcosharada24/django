from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name="index"),  # Página inicial
    
    # Usuários
    path('usuarios/', views.exibirUsuarios, name="exibirUsuarios"),
    path('add-usuario/', views.addUsuario, name="addUsuario"),
    path('excluir-usuario/<int:id_usuario>/', views.excluirUsuario, name="excluirUsuario"),
    path('editar-usuario/<int:id_usuario>/', views.editarUsuario, name="editarUsuario"),
    
    # Produtos
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('produtos/novo/', views.cadastrar_produto, name='cadastrar_produto'),
    path('produtos/editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('produtos/excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Produtos - cards view
    path('produtos/cards/', views.produtosCards, name='produtos_cards'),
]
