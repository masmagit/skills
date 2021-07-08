from django.urls import path
from . import views

app_name = 'collection'
urlpatterns = [
    path('', views.collect, name='collect'),
    path('q/<int:opt>', views.queries, name='queries'),
]