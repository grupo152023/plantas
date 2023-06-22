
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegistroUsuario

# Create your views here.

def mi_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            nxt = request.GET.get("next", None)
            if nxt is None:
                return redirect("inicio")
            else:
                return redirect(nxt)
        else:
            messages.error(request,"Usuario o contraseña incorrecta")

    form = AuthenticationForm()
    return render(request, 'login-registro/login.html', {"form":form})

def cerrar_sesion(request):
    logout(request)
    return redirect("inicio")

class Registro(View):
    def get(self, request):
        form = RegistroUsuario()
        return render(request, 'login-registro/registro.html',{"form":form})

    def post(self, request):
        form = RegistroUsuario(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request,usuario)
            return redirect("inicio")
        else: #NO FUNCIONA CUANDO DA ERROR
            for  msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
       
            return render(request, 'login-registro/registro.html',{"form":form})




   
   