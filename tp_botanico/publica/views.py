from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from django.conf import settings

from .models import Producto
from .models import Planta

from .forms import contacto_form, Post_form
from .models import *

# Create your views here.

def index(request):
    return render(request, 'publica/index.html')

def nosotros(request):
    return render(request, 'publica/nosotros.html')

def staff(request):
    return render(request, 'admin')

def productos(request):
    wambi = request.GET.get('Ambientes')
    #print(a) 
    if wambi=="Todos" or wambi==None:
       listado_productos = Producto.objects.all()
    else:
       listado_productos = Producto.objects.all().filter(ambiente=wambi)
    #listado_productos = Producto.objects.filter(precio__range=(1200, 9999))
    return render(request, 'publica/productos.html', {"productos":listado_productos})

def plantas(request):
    wambi = request.GET.get('Ambientes')
    #print(a) 
    if wambi=="Todos" or wambi==None:
       listado_productos = Planta.objects.all()
    else:
       listado_productos = Planta.objects.all().filter(ambiente=wambi)
    #listado_productos = Producto.objects.filter(precio__range=(1200, 9999))
    return render(request, 'publica/productos.html', {"productos":listado_productos})


def productocaro(request):
    listado_productos = Producto.objects.filter(precio__range=(5000, 9999999999))
    return render(request, 'publica/productos.html', {"productos":listado_productos})

def productobarato(request):
    listado_productos = Producto.objects.filter(precio__range=(1, 4999))
    #listado_productos = Producto.objects.all().filter(ambiente=loque)

    return render(request, 'publica/productos.html', {"productos":listado_productos})


def contacto(request):
    mensaje = None #Ver clase 17
    #Si recibe la URL por POST toma los datos del formulario
    if request.method == "POST":
        formContacto = contacto_form(request.POST)
        #Se valida los datos is_valid()
        if formContacto.is_valid():
            messages.info(request,"El formulario se ha enviado con exito!")
            mjs = f'De: {formContacto.cleaned_data["nombre"]}, mail: {formContacto.cleaned_data["mail"]}, asunto: {formContacto.cleaned_data["asunto"]}, mensaje: {formContacto.cleaned_data["mensaje"]}'
            mjs_html = f"""
                <p>De: {formContacto.cleaned_data["nombre"]} <a href="mailto:{formContacto.cleaned_data["mail"]}">
                {formContacto.cleaned_data["mail"]}</a></p>
                <p>Asunto: {formContacto.cleaned_data["asunto"]}</p>
                <p>mensaje: {formContacto.cleaned_data["mensaje"]}</p>
            """  
            asunto = f"CONSULTA DE LA PÁGINA: {formContacto.cleaned_data['asunto']}"
            send_mail(
                asunto,
                mjs,
                settings.EMAIL_HOST_USER,
                [settings.RECIPIENT_ADDRESS],
                fail_silently=False,
                html_message=mjs_html
            )
            formContacto = contacto_form()      
        else:
          messages.info(request,"Error: verificar los campos del formulario")           
    #Si la URL es recibida por el metodo GET crea un formulario en blanco (sin datos)
    else:
        formContacto = contacto_form()
    return render(request, "publica/contacto.html", {"formContacto": formContacto})
    
@login_required
def club(request):
    posts = Post.objects.all()    
    return render(request, 'publica/club.html', {"posts": posts})

def post(request):
    get_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == "POST":
        form = Post_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = get_user
            post.save()
            messages.success(request, "Tu post ha sido creado!")
            return redirect("club")
    else:
        form = Post_form()
    return render(request, 'publica/crearPost.html', {"form": form})

def perfil(request,username=None):
    get_user = request.user
    if username and username != get_user.username:
        user = User.objects.get(username=username)
        posts = user.post.all()
    else:
        posts = get_user.post.all()
        user = get_user

    context = {
        'user':user,
        'posts':posts
    }
    return render(request, 'publica/perfil.html', context)

def seguir(request, username):
    get_user = request.user
    a_user = User.objects.get(username=username)
    a_user_id = a_user
    rel = Relacion(desde_user=get_user, a_user=a_user_id)
    rel.save()
    return redirect('club')

def noSeguir(request, username):
    get_user = request.user
    a_user = User.objects.get(username=username)
    a_user_id = a_user
    rel = Relacion.objects.filter(desde_user=get_user.id, a_user=a_user_id).get()
    rel.delete()
    return redirect('club')
