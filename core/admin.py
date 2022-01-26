from django.contrib import admin
from django.contrib.auth import get_user_model
from core.models import Responder, Questionnaire, Question, SubQuestion, SubQuestionAnswer, Interrogator, \
    ResultQuestionnaire

User = get_user_model()


@admin.register(Interrogator)
class InterrogatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'completed_questionnaires')
    readonly_fields = ('completed_questionnaires',)

    def get_queryset(self, request):
        return Interrogator.objects.filter(user=request.user)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super(QuestionAdmin, self).get_form(request, obj, change, **kwargs)
        form.base_fields['creator'].queryset = Interrogator.objects.filter(user=request.user)
        return form

    def get_queryset(self, request):
        questions = Question.objects.filter(creator=request.user.interrogator)
        return questions

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user.interrogator
        return super(QuestionAdmin, self).save_model(request, obj, form, change)


@admin.register(SubQuestion)
class SubQuestionAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super(SubQuestionAdmin, self).get_form(request, obj, change, **kwargs)
        form.base_fields['question'].queryset = Question.objects.filter(creator=request.user.interrogator)
        form.base_fields['creator'].queryset = Interrogator.objects.filter(user=request.user)
        return form

    def get_queryset(self, request):
        sub_questions = SubQuestion.objects.filter(creator=request.user.interrogator)
        return sub_questions

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user.interrogator
        return super(SubQuestionAdmin, self).save_model(request, obj, form, change)


@admin.register(SubQuestionAnswer)
class SubQuestionAnswerAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super(SubQuestionAnswerAdmin, self).get_form(request, obj, change, **kwargs)
        form.base_fields['sub_question'].queryset = SubQuestion.objects.filter(creator=request.user.interrogator)
        form.base_fields['creator'].queryset = Interrogator.objects.filter(user=request.user)
        return form

    def get_queryset(self, request):
        sub_question_answers = SubQuestion.objects.filter(creator=request.user.interrogator)
        return sub_question_answers

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user.interrogator
        return super(SubQuestionAnswerAdmin, self).save_model(request, obj, form, change)


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super(QuestionnaireAdmin, self).get_form(request, obj, change, **kwargs)
        form.base_fields['interrogator'].queryset = Interrogator.objects.filter(user=request.user)
        return form

    list_display = ('interrogator', 'responder')


admin.site.register(Responder)
# admin.site.register(Questionnaire)
# admin.site.register(Question)
# admin.site.register(SubQuestion)
# admin.site.register(SubQuestionAnswer)
admin.site.register(ResultQuestionnaire)
