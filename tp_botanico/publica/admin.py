from django.contrib import admin
from .models import Producto, Perfil, Post, Relacion
from .models import Planta
from .models import TipoPlanta,GrupoPlanta


# Register your models here.
admin.site.register(Producto)
admin.site.register(Perfil)
admin.site.register(Post)
admin.site.register(Relacion)

admin.site.register(Planta)

admin.site.register(TipoPlanta)
admin.site.register(GrupoPlanta)
