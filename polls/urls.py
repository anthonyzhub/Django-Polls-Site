# OBJECTIVE: Link a view to a URL path

from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='index')]