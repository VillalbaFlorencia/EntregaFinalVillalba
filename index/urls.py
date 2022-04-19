from django.urls import path
from .views import index, recomendadas

urlpatterns = [
    path('', index, name = 'index'),
    #path('recomendadas/', recomendadas, name = 'recomendadas'),   
]
