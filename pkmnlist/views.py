from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from pkmnlist.dictionarys import generation
from .models import pkmnlist


def index(request):
    pkmnlists = pkmnlist.objects.order_by('pokedex_number')  # .filter(is_published=True)

    context = {
        'pkmnlists': pkmnlists,
        'generation': generation
    }

    return render(request, 'pkmnlists/pkmnlists.html', context)


def pkmnlists(request, pkmnlist_id):
    pkmnpage = get_object_or_404(pkmnlist, pk=pkmnlist_id)
    context = {
        'pkmnpage': pkmnpage,
        'generation': generation
    }
    return render(request, 'pkmnlists/pkmnpage.html', context)


def search(request):
    queryset_list = pkmnlist.objects.order_by('pokedex_number')

    # URL Keywords past by POST
    if 'pkmnname' in request.POST:
        pkmnsearchedname = request.POST['pkmnname']
    if pkmnsearchedname:
        queryset_list = queryset_list.filter(name__icontains=pkmnsearchedname)

    context = {
        'pkmnlists': queryset_list,
        'generation': generation
    }
    return render(request, 'pkmnlists/search.html', context)


def generations(request):

    # URL Keywords past by POST
    if 'pkmngeneration' in request.POST:
        pkmngeneration = request.POST['pkmngeneration']
    if pkmngeneration:
        generationpage = pkmnlist.objects.order_by('pokedex_number').filter(generation=pkmngeneration)
    context = {
        'pkmnlists': generationpage,
        'generation': generation,
        'pkmngeneration': pkmngeneration
    }

    return render(request, 'pkmnlists/pkmnlists.html', context)
