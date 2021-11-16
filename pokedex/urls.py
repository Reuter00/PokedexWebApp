
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pkmnlist.urls')),
    path('pkmnlist/', include('pkmnlist.urls')),
    path('admin/', admin.site.urls),
]
