from django.urls import path

from .views import login, registrar, editar, about, usuario_datos
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', login, name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'accounts/logout.html'), name = 'logout'),
    path('registrar/', registrar, name = 'registrar'),
    path('editar/', editar, name = 'editar'),
    path('about/', about, name = 'about'),
    path('datos/', usuario_datos, name='usuario_datos'),
]

