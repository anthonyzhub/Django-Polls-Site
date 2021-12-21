# OBJECTIVE: Link a view to a URL path

from django.urls import path
from . import views

urlpatterns = [
    # E.g., /polls/
    path('', views.index, name='index'),
    
    # E.g., /polls/<question_id>/
    path('<int:question_id>/', views.detail, name='detail'),
    
    # E.g., /polls/<question_id>/results/
    path('int:question_id>/results/', views.results, name='results'),
    
    # E.g., /polls/<question_id>/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')
]