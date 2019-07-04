from django.contrib import admin
from .models import Question,Choice
# Register your models here.

#class Choiceadd(admin.StackedInline):
class Choiceadd(admin.TabularInline):
    model=Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    #fields=['question_text','pub_date']
    list_display = ('question_text', 'pub_date','was_published_recently')
    fieldsets=[
        ('Question', {'fields':['question_text']}),
        ('Date information',{'fields':['pub_date']})
    ]
    inlines=[Choiceadd]

admin.site.register(Question,QuestionAdmin)

#admin.site.register(Choice)
