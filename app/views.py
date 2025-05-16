from django.shortcuts import render, redirect, get_object_or_404
from app.models import Usuario, Produto
from app.forms import formUsuario, formProduto
import requests
# INDEX
def index(request):
    return render(request, "index.html")

# EXIBIR USUÁRIOS (com verificação de sessão)
def exibirUsuarios(request):
    if not request.session.get('usuario_id'):
        return redirect('index')
    
    usuarios = Usuario.objects.all()
    return render(request, "usuarios.html", {'listUsuarios': usuarios})

# ADICIONAR USUÁRIO
def addUsuario(request):
    form = formUsuario(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('exibirUsuarios')
    
    return render(request, "add-usuario.html", {'form': form})

# EXCLUIR USUÁRIO
def excluirUsuario(request, id_usuario):
    if not request.session.get('usuario_id'):
        return redirect('index')

    usuario = get_object_or_404(Usuario, id=id_usuario)
    usuario.delete()
    return redirect('exibirUsuarios')

# EDITAR USUÁRIO
def editarUsuario(request, id_usuario):
    if not request.session.get('usuario_id'):
        return redirect('index')

    usuario = get_object_or_404(Usuario, id=id_usuario)
    form = formUsuario(request.POST or None, instance=usuario)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('exibirUsuarios')

    return render(request, "editar-usuario.html", {'form': form})

# CADASTRAR PRODUTO
def cadastrarProduto(request):
    if not request.session.get('usuario_id'):
        return redirect('index')

    form = formProduto(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('listarProdutos')
    
    return render(request, "cadastrar-produto.html", {'form': form})

# LISTAR PRODUTOS
def listarProdutos(request):
    if not request.session.get('usuario_id'):
        return redirect('index')

    produtos = Produto.objects.all()
    return render(request, "listar-produtos.html", {'produtos': produtos})

# EXCLUIR PRODUTO
def excluirProduto(request, id_produto):
    if not request.session.get('usuario_id'):
        return redirect('index')

    produto = get_object_or_404(Produto, id=id_produto)
    produto.delete()
    return redirect('listarProdutos')

# EDITAR PRODUTO
def editarProduto(request, id_produto):
    if not request.session.get('usuario_id'):
        return redirect('index')

    produto = get_object_or_404(Produto, id=id_produto)
    form = formProduto(request.POST or None, request.FILES or None, instance=produto)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('listarProdutos')

    return render(request, "editar-produto.html", {'form': form})

def produtos(request):
 prosutosapi = request.get("https://fakestoreapi.com/products").json()
 return render(request,"produtos.html",{'prdoutos':produtosapi})

# DASHBOARD
def dashboard(request):
    if not request.session.get('usuario_id'):
        return redirect('index')

    total_usuarios = Usuario.objects.count()
    total_produtos = Produto.objects.count()

    return render(request, "dashboard.html", {
        'total_usuarios': total_usuarios,
        'total_produtos': total_produtos,
    })
