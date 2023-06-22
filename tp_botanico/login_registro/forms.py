from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuario(UserCreationForm):
	username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={'class': 'registro-campo'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'registro-campo'}))
	first_name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class': 'registro-campo'}))
	last_name = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={'class': 'registro-campo'}))
	password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'registro-campo'}))
	password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput(attrs={'class': 'registro-campo'}))
	

	class Meta():
		model= User
		fields = ['username','first_name','last_name','email','password1','password2']
		help_text = {k:"" for k in fields}




