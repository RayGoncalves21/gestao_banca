from django.shortcuts import render


def home(request):
    return render(request, 'pagina_inicial/paginas/home.html')
