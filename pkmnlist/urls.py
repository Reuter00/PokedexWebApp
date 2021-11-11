from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='pkmnlists'),
    path('<int:pkmnlist_id>', views.pkmnlists, name='pkmnpage'), # Passing id and acessing it
    path('search', views.search, name='search')
]