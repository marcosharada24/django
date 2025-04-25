from urllib import request
from django.shortcuts import redirect, render
from app.models import Usuario
from app.forms import formUsuario

def index(request):
    return render(request, "index.html")
    
def exibirUsuarios(request):
 usuarios = usuarios.objects.all().values()
 return render(request, "usuraios.html",
{'listUsuarios':usuarios})

def addUsaurio(request):
   fromUsers = formUsuario(request.POST or None)
if request.POST:
   if formUsuario.is_valid():
      formUsuario.save() 
      return redirect("exibirUsuarios")
   
    return render(request, "add-usuario.html", {'form': formUser})
   
def excluirUsuario(request, id_usuario):
   usuario = Usuario.objects.get(id=id_usuario)
   usuario.delete()
   return redirect("exibirUsuarios")

def editarUsuario(request, id_usuario):
   usuario = Usuario.objects.get(id=id_usuario)
  
   formUsuario = formUsuario(request.POST or None, instance=usuario)

   if request.POST:
    if formUsuario.valid():
      formUsuario.save()
      return redirect("exibirUsuarios")
    
   return  render(request,"editar-usuario.html",
   {'form' : formUsuario})

def produto(request, imagem):
   if request.method == 'POST':
      form = FotoForm(request.POST, request.FILES)
  <form method="post" enctype="multipart/form-data">
      {% csrf_token %}
      {{ form.as_p }}
      <button type="submit">enviar</button>
   </form>

def cadastrarProduto(request):
   fromProduto = formProduto(request.POST or None)
if request.POST:
   if formProduto.is_valid():
      formProduto.save() 
      return redirect("produtos")
   
def listarProdutos(request):
produtos = produtos.objects.all().values()



def excluirProdutos(request):
   produtos = Usuario.objects.get()
   produtos.delete()
   
def editarProdutos(request):
   produtos= Usuario.objects.get()