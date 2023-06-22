from . import views
from django.urls import path
from .views import Registro
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.mi_login, name='login'),
    path('registro', Registro.as_view(), name='registro'), 
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),    
    path('reset_password/', auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('accounts/login/',views.mi_login,name="sesion_requerida")
]
