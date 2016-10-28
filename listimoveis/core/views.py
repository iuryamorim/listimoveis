from django.shortcuts import render

from listimoveis.imoveis.models import Imovel


def home(request):
    if request.method == 'GET':
        try:
            q = request.GET.get('q', None)
        except:
            q = None

        if q:
            return search(request, q)

        imoveis = Imovel.objects.all().order_by('-created_at')[:9]
        return render(request, 'index.html', {'imoveis': imoveis})


def search(request, search):
    try:
        imovel_busca = Imovel.objects.all().filter( address__contains=search )
        if not imovel_busca:
            return render(request, 'index.html', {'error': True})
    except:
        return render(request, 'index.html', {'error': True})

    try:
        cep = imovel_busca[0].cep[:5]
        imoveis_rel = Imovel.objects.all().filter( cep__contains=cep )
        print(len(imovel_busca) + len(imoveis_rel))
        print(len(imovel_busca))
        if (len(imovel_busca) * 2) == (len(imovel_busca) + len(imoveis_rel)):
            return render(request, 'index.html', {'imoveis': imovel_busca, 'alert': True})
    except:
        return render(request, 'index.html', {'imoveis': imovel_busca, 'alert': True})

    imoveis = list()
    for i in imovel_busca:
        imoveis.append(i)
    for i in imoveis_rel:
        if i not in imoveis:
            imoveis.append(i)
    return render(request, 'index.html', {'imoveis': imoveis})