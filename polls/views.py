from typing import Generic
from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Question, Choice

# Create your views (webpage) here.
"""
generic.ListView => display a list of objects
generic.DetailView => Display a detail page for a specific object
"""
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-publication_date")

class DetailView(generic.DetailView):

    model = Question # <= Each generic view needs to know what modeil it will be acting upon
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question # <= Each generic view needs to know what modeil it will be acting upon
    template_name = "polls/results.html"

def vote(request, question_id):

    # OBJECTIVE: Display results for a particular question
    
    # Get question or 404 error message
    question = get_object_or_404(Question, pk=question_id)

    # Get vote
    try:

        # Filter POST data by getting "choice" string
        # NOTE: request.POST is a dictionary
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    
    # If "choice" is not found, return error message
    except (KeyError, Choice.DoesNotExist):

        # Create a dict for future use
        context = {
            "question": question,
            "error_message": "You didn't select a choice"
        }

        # Return HttpRepsonse with "detail.html" format
        return render(request, "polls/detail.html", context)

    else:

        # Increment vote and save change in database
        selected_choice.votes += 1
        selected_choice.save()

        # Return HttpResponseRedirect to redirect user after handling POST data
        # NOTE: This will prevent a double vote in case user clicks "back" button
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))