from django.contrib import admin

from .models import Question, Choice

admin.site.register(Question)

admin.site.register(Choice)


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
    list_display = ('question_text', 'pub_date')


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']



