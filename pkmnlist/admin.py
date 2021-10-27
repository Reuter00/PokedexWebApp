from django.contrib import admin
from .models import pkmnlist


class PkmnlistAdmin(admin.ModelAdmin):
    list_display = ('pokedex_number', 'name', 'generation', 'type_1', 'type_2')
    list_display_links = ('pokedex_number', 'name')  # clickble link
    list_filter = ('generation', 'type_1', 'type_2', 'ability_1', 'ability_2',
                   'ability_hidden')  # filter box
    search_fields = ('name', )  # , 'generation', 'type_1', 'type_2', 'ability_1', 'ability_2',
    # 'ability_hidden'

    list_per_page = 25


admin.site.register(pkmnlist, PkmnlistAdmin)
