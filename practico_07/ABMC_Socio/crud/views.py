from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Socio
from .forms import SocioForm


def index(request):
    return render(request, 'templates/index.html')


def list_socios(request):
    socios = Socio.objects.all()
    return render(request, 'templates/list_socios.html', {'socios': socios, })


def create(request):
    form = SocioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'templates/create_form.html', {'form': form})  #Accede directamente al primer directorio llamado templates


def delete(request, id):
    socio = Socio.objects.get(id_socio=id)
    socio.delete()
    return redirect('list')


def update(request, id):
    socio = Socio.objects.get(id_socio=id)
    form = SocioForm(request.POST or None, instance=socio)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('list')
    return render(request, 'templates/update_form.html', {'form': form, })

