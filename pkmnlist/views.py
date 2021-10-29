from django.core.paginator import Paginator
from django.shortcuts import render

from .models import pkmnlist


def index(request):
    pkmnlists = pkmnlist.objects.all()  # order_by('-list_date').filter(is_published=True)

    #  paginator = Paginator(pkmnlists, 2)
    # page = request.GET.get('page')
    # paged_listings = paginator.get_page(page)

    context = {
        'pkmnlists': pkmnlists
    }

    return render(request, 'pkmnlists/pkmnlists.html', context)


# return render(request, 'pkmnlists/pkmnlists.html')


def pkmnlists(request):
    return render(request, 'pkmnlists/pkmnlists.html')


def search(request):
    return render(request, 'pkmnlists/search.html')
