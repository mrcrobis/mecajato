from django.shortcuts import render
from django.http import HttpResponse

# request = requisicao do usuario
def clientes(request):
    return render(request, 'clientes.html')