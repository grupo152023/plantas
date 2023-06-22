from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('contacto', views.contacto, name='contacto'),
    path('productos', views.productos, name='productos'),
    path('plantas', views.plantas, name='plantas'),
    path('club', views.club, name='club'),
    path('crearpost', views.post, name='crearpost'),
    path('perfil', views.perfil, name='perfil'),
    path('perfil/<str:username>', views.perfil, name='crearpost'),
    path('seguir/<str:username>', views.seguir, name='seguir'),
    path('noseguir/<str:username>', views.noSeguir, name='noseguir'),
    path('productocaro/', views.productocaro, name='productocaro'),
    path('productobarato', views.productobarato, name='productobarato'),
    path('Staff', views.staff, name='Staff'),
]
