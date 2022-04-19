from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NuestraCreacionUser(UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput())
    password2 = forms.CharField(label = 'Repetir Contraseña', widget = forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = { k: '' for k in fields }
    
    
class NuestraEdicionUser(forms.Form):
    
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput(), required = False)
    password2 = forms.CharField(label = 'Repetir Contraseña', widget = forms.PasswordInput(), required = False)
    first_name = forms.CharField(label = 'Nombre', max_length=20, required = False)
    last_name = forms.CharField(label = 'Apellido', max_length=20, required = False)
    imagen = forms.ImageField(required = False)
    link = forms.URLField(required = False)
    more_description = forms.CharField(required = False, max_length=100)
  