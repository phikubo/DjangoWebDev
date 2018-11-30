from django.shortcuts import render
from django.contrib.auth import authenticate, get_user_model,login,logout
# Create your views here.
from . formulario import UsuarioLoginForm

def entrar_views(request):
    formulario=UsuarioLoginForm(request.POST or None)
    if request.user.is_authenticated:
        print("Log in")
    if formulario.is_valid():
        print("isvalid")
        usuario=formulario.cleaned_data.get("NombreUsuario")
        contrasena=formulario.cleaned_data.get("Contrasena")
        user=authenticate(username=usuario,password=contrasena)
        print("isvalid1")
        login(request,user)
    print("El formulario es invalido")    
    return render(request, "cuentas/entrarlogin.html", {"formulario":formulario})

def registrar_views(request):
    return render(request, "index.html", {})
    
def salir_views(request):
    return render(request, "index.html", {})