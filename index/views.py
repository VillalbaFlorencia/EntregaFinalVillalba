from django.shortcuts import render


def index(request):
    return render(request, 'index/index.html', {})

def recomendadas(request):
    
    datos = {
        'lista' : ['Game Of Thrones', 'Breaking Bad', 'Vikingos', 'Peaky Blinders', 'The Walking Dead'],
    }
    
    return render(request, 'index/recomendadas.html', datos)

