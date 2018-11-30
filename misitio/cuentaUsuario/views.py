from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
#

def index(request):
    return render(request,'cuentaUsuario/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            nombreUsuario=form.cleaned_data['username']
            clave=form.cleaned_data['password1']
            usuario=authenticate(username=nombreUsuario,password=clave)
            login(request,usuario)
            return redirect('/index')
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request, 'registration/registration.html', context)

#https://www.youtube.com/watch?v=dBctY3-Z5hY