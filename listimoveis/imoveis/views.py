from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r, get_object_or_404
from listimoveis.imoveis.forms import ImoveisForm
from listimoveis.imoveis.models import Imovel


def new(request):
    if request.method == 'POST':
        return create(request)
    return empty_form(request)


def empty_form(request):
    return render(request, 'imoveis/imovel-form.html', {'form': ImoveisForm()})


def create(request):
    form = ImoveisForm(request.POST, request.FILES)
    if not form.is_valid():
        return render(request, 'imoveis/imovel-form.html', {'form': form})

    imovel = form.save()

    return HttpResponseRedirect(r('home'))


def detail(request, slug):
    imovel = get_object_or_404(Imovel, slug=slug)
    return render(request, 'imoveis/imovel_detail.html', {'imovel': imovel})


def alter(request, slug):
    if request.method == 'POST':
        return update(request, slug)
    return update_form(request, slug)

def delete(request, slug):
    data = get_object_or_404(Imovel, slug=slug)
    data.delete()
    return HttpResponseRedirect(r('home'))


def update_form(request, slug):
    imovel = get_object_or_404(Imovel, slug=slug)
    form = ImoveisForm(initial={'name': imovel.name, 'address': imovel.address, 'cep': imovel.cep,
                                'slug': imovel.slug, 'photo': imovel.photo, 'description': imovel.description})
    return render(request, 'imoveis/imovel_alter.html', {'form': form})


def update(request, slug):
    data = get_object_or_404(Imovel, slug=slug)
    form = ImoveisForm(request.POST, request.FILES)
    if not form.is_valid():
        return render(request, 'imoveis/imovel_alter.html', {'form': form})
    imovel = form.save(commit=False)
    imovel.created_at = data.created_at
    imovel.id = data.pk
    imovel.save()

    return HttpResponseRedirect(r('home'))
