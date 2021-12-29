from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):

    # NOTE: The 1st element of each tuple is the title of the field set
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["publication_date"], "classes": ["collapse"]})
    ]

    inlines = [ChoiceInLine]

    # Add columns with details
    list_display = ["question_text", "publication_date", "was_published_recently"]

    # Add filter capability
    list_filter = ["publication_date"]

    # Add search capability
    # I.e., Admin can search for questions
    search_fields = ["question_text"]

# Add Question field to admin site
admin.site.register(Question, QuestionAdmin)