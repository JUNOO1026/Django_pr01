from django.urls import utils
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
