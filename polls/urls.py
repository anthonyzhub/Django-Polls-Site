# OBJECTIVE: Link a view to a URL path

from django.urls import path
from . import views

# Add namespace for Django to distinguish apps
app_name = "polls"

urlpatterns = [
    # E.g., /polls/
    path('', views.IndexView.as_view(), name='index'),
    
    # E.g., /polls/<primary key>/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    
    # E.g., /polls/<primary key>/results/
    path('int:pk>/results/', views.ResultsView.as_view(), name='results'),
    
    # E.g., /polls/<question_id>/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')
]