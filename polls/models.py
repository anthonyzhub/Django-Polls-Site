"""
Remember the three-step guide to making model changes:

    1. Change your models (in models.py).
    2. Run 'python manage.py makemigrations' to create migrations for those changes
    3. Run 'python manage.py migrate' to apply those changes to the database.

"""
from django.db import models
from django.utils import timezone
from django.contrib import admin

from datetime import timedelta

# Create your models here.

# OBJECTIVE: Create a new model called "Question" where it will hold a question and publication date
class Question(models.Model):

    # Class variables
    question_text = models.CharField(max_length=200)
    publication_date = models.DateTimeField("Date Published")

    def __str__(self):
        # OBJECT: When object is called, return quesiton_text
        return self.question_text

    @admin.display(
        boolean=True,
        ordering="publication_date",
        description="Published recently?"
    )

    def was_published_recently(self):
        
        # Get current time
        now = timezone.now()

        # Return True, if (1) it's been less than a day, (2) publication date is older than current time, (3) "now" is newer than "publication_date"
        # I.e. Return True if question is ONLY less than a day old
        return now - timedelta(days=1) <= self.publication_date <= now

# OBJECTIVE: Create a new model called "Choice" where it will hold a Question instance, text of choice, and a vote tally
class Choice(models.Model):

    # Class variables
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) # <= Default value is "0" votes

    # When object is called, return choice_text
    def __str__(self):
        return self.choice_text