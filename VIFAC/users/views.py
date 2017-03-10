from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    context = {}
    return render(request, 'users/crear.html', context)

def modificar(request):
	context = {}
	return render(request, 'users/modificar.html', context)

def borrar(request):
	context = {}
	return render(request, 'users/borrar.html', context)

def consultar(request):
	context = {}
	return render(request, 'users/consultar.html', context)