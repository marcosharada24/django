from urllib import request
from django.shortcuts import redirect, render
from app.models import Usuario
from app.forms import formUsuario

def index(request):
    return render(request, "index.html")
    
def exibirUsuarios(request):
 usuarios = usuarios.objects.all().values()
 return render(request, "usauraios.html",
{'listUsuarios':usuarios})

def addUsaurio(request):
   fromUser = formUsuario(request.POST or None)
if request.POST:
   if formUser.is_valid():
      formUser.save() 
     return redirect("exibirUsuarios")
   
context = {
     'form' : formUsuario
  }
   
 return render(request, "add-usuario.html", context)