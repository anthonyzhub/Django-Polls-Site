from datetime import timedelta
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question

def create_question(question_text, days):
    
    # OBJECTIVE: A global function to create a new question for testing purposes

    time = timezone.now() + timedelta(days=days)
    return Question.objects.create(question_text=question_text, publication_date=time)

# Create your tests here.
# NOTE: Functions must start with the word "test"

class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        
        # OBJECTIVE: If no questions exist, display a message

        # Get response from web page
        response = self.client.get(reverse("polls:index"))

        # Compare results
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):

        # OBJECTIVE: Create a question and verifies that it appears

        # Create a test question
        question = create_question(question_text="Past question", days=-30)

        # Get web page response
        response = self.client.get(reverse("polls:index"))

        # Compare results
        # NOTE: "response" should have a list of the question we just created
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])

    def test_future_question(self):

        # OBJECTIVE: Create a future question and verify that it doesn't appear
        # I.e., Make sure a question set for the future isn't shown in the present

        # Create a test question in the future
        create_question(question_text="Future question", days=30)

        # Get response
        response = self.client.get(reverse("polls:index"))

        # Compare results
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):

        # OBJECTIVE: Even if both past and future questions exist, only past questions are displayed

        # Create an old and a future question
        question = create_question(question_text="Past question", days=-30)
        create_question(question_text="Future question", days=30)

        # Get response
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])

    def test_two_past_questions(self):

        # OBJECTIVE: Create 2 old questions and verify they are presented in oldest-newest order

        # Create 2 old questions
        question1 = create_question(question_text="Past question 1", days=-30)
        question2 = create_question(question_text="Past question 2", days=-5)

        # Get response
        response = self.client.get(reverse("polls:index"))

        # Compare results
        self.assertQuerysetEqual(response.context["latest_question_list"], [question2, question1])

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):

        # OBJECTIVE: was_published_recently() returns False for questions whose publication_date is in the future

        # Get current time and add 30 days
        time  = timezone.now() + timedelta(days=30)

        # Create a new question that has a publication date from the future
        future_question = Question(publication_date=time)

        # Assert that the was_published_recently() returns false.
        # If not, then test failed and program will crash
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):

        # OBJECTIVE: was_published_recently() returns False for questions whose publication_date is older than 1 day

        # Create a one day and second old question
        time = timezone.now() - timedelta(days=1, seconds=1)
        old_question = Question(publication_date=time)

        # was_published_recently() must return false
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):

        # OBJECTIVE: was_published_recently() returns True for questions whose publication_date is within the last day

        # Create a question that was created within the last 24 hours
        time = timezone.now() - timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(publication_date=time)

        # was_published_recently() must return true
        self.assertIs(recent_question.was_published_recently(), True)