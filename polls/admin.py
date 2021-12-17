from django.contrib import admin
from .models import Question

# Register your models here.

# Add Question field to admin site
admin.site.register(Question)