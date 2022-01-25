from django.contrib import admin

# Register your models here.
from core.models import Responder, Questionnaire, Question, SubQuestion, Answer

admin.site.register(Responder)
admin.site.register(Questionnaire)
admin.site.register(Question)
admin.site.register(SubQuestion)
admin.site.register(Answer)