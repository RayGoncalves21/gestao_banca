from django.urls import path

from inicio.views import home

urlpatterns = [
    path('', home),  # Home


]
