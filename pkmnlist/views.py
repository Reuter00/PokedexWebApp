from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from pkmnlist.dictionarys import generation
from .models import pkmnlist


def index(request):
    pkmnlists = pkmnlist.objects.order_by('pokedex_number')  # .filter(is_published=True)

    # paginator = Paginator(pkmnlists, 2)
    # page = request.GET.get('page')
    # paged_listings = paginator.get_page(page)

    context = {
        'pkmnlists': pkmnlists,
        'generation': generation
    }

    return render(request, 'pkmnlists/pkmnlists.html', context)


# return render(request, 'pkmnlists/pkmnlists.html')


def pkmnlists(request, pkmnlist_id):
    pkmnpage = get_object_or_404(pkmnlist, pk=pkmnlist_id)
    context = {
        'pkmnpage': pkmnpage
    }
    return render(request, 'pkmnlists/pkmnpage.html', context)


def search(request):
    queryset_list = pkmnlist.objects.order_by('pokedex_number')

    # URL Keywords
    if 'pkmnname' in request.GET:
        pkmnsearchedname = request.GET['pkmnname']
    if pkmnsearchedname:
        queryset_list = queryset_list.filter(name__icontains=pkmnsearchedname)

    context = {
        'pkmnlists': queryset_list

    }
    return render(request, 'pkmnlists/search.html', context)
