from django import forms
from ckeditor.fields import RichTextFormField


class SerieFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    categoria = forms.CharField(max_length=30)
    netflix = forms.BooleanField(required = False)
    descripcion = RichTextFormField(required = False)
    
    
class PeliculaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    categoria = forms.CharField(max_length=30)
    netflix = forms.BooleanField(required = False)
    descripcion = RichTextFormField(required = False)
    

class SerieBusqueda(forms.Form):
    nombre = forms.CharField(max_length=30)
    
class PeliculaBusqueda(forms.Form):
    nombre = forms.CharField(max_length=30)
    