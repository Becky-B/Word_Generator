from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('count', views.count),
    path('reset', views.reset)
]