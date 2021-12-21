from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Question

# Create your views (webpage) here.
def index(request):

    # OBJECTIVE: Get the last 5 questions based on publication date

    # Get the last 5 questions
    try:
        latest_question_list = Question.objects.order_by("-publication_date")[:5]

    # If there aren't any quesitons, return 404
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    
    """
    === METHOD 1 ===:

    # Load template for index page
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list} # <= Maps template variable names to Python objects

    # Return questions with template format
    return HttpResponse(template.render(context, request))
    """
    
    # === Method 2 ===

    # Map template variable name to Python object
    context = {"latest_question_list": latest_question_list}

    # Return HttpResponse with template format
    # NOTE: render(<request object>, <template path>, [dictionary])
    return render(request, "polls/index.html", context)

def detail(request, question_id):

    # OBJECTIVE: Display latest few questions

    # Get question based on id
    # NOTE: If question is not found, return HTTP 404 error
    question = get_object_or_404(Question, pk=question_id)

    # Map template variable name to Python object
    context = {"question": question}

    # Return question in template format
    return render(request, "polls/detail.html", context)

def results(request, question_id):
    # OBJECTIVE: Display a question text without any results by with a form to vote
    return HttpResponse(f"You're looking at the results of question '{question_id}'")

def vote(request, question_id):
    # OBJECTIVE: Display results for a particular question
    return HttpResponse(f"You're voting on question '{question_id}'")