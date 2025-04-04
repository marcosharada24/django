from django import forms
from app.models import Usuario 

class formUsuario(forms.Modelform):
    class Meta:
        model = Usuario
        fields = ('nome','email','senha')

        widgets = {
            'nome' : forms.TextInput(attrs={'type':'text'}),
            'email' : forms.TextInput(attrs={'type':'email'}),
            'senha' : forms.TextInput(attrs={'type':'passsword'})
        }   