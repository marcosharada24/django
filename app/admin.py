from django.contrib import admin
from .models import Usuario

class UsuarioAdimin(admin.ModelAdmin):
    list_display = ("nome","email","senha")

admin.site.register(Usuario, UsuarioAdimin)
