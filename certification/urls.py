from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.home, name='home'),
]