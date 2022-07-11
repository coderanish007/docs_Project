from django.contrib import admin
from . models import Question, Choices

# Register your models here.

class ChoiceInLine(admin.StackedInline): #TabularInLine
    model = Choices
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldset = [
        (None, {'fields': ['question_text']}),
        ('Date information',{'fields': ['pub_date'],'classes':['collapse']}),
        ]
    inlines = [ChoiceInLine]

admin.site.register(Question,QuestionAdmin)