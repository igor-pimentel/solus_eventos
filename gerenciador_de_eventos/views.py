from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Solus Eventos</h1><p> Bem vindo ao Gerenciador de Eventos da Solus|IT')

    
