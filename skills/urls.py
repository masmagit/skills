from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('collection/', include('collection.urls')),
    #path('', RedirectView.as_view(url='main/', permanent=True)),
]
