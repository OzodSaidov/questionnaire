from django.db import models
from config.base_models import BaseModel
from user.models import Interrogator


class Responder(BaseModel):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    birth_date = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER)


class Questionnaire(BaseModel):
    responder = models.ForeignKey(Responder, on_delete=models.CASCADE, related_name='questionnaires')
    interrogator = models.ForeignKey(Interrogator, on_delete=models.CASCADE, related_name='questionnaires')
    questions = models.ManyToManyField('Question')
    is_completed = models.BooleanField(default=False)


class Question(BaseModel):
    ANSWER = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    question_text = models.TextField()
    answer = models.CharField(max_length=3, choices=ANSWER, blank=True, null=True)
    sub_question = models.OneToOneField('SubQuestion', on_delete=models.SET_NULL, null=True)


class SubQuestion(BaseModel):
    question_text = models.TextField()


class Answer(BaseModel):
    sub_question = models.ForeignKey(SubQuestion, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(max_length=255)
    is_marked = models.BooleanField(default=False)
