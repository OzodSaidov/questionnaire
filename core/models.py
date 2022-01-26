from django.db import models
from config.base_models import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Interrogator(BaseModel):
    """
    Опросчик
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def completed_questionnaires(self) -> int:
        return self.questionnaires.count()


class Responder(BaseModel):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    birth_date = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER)


class Questionnaire(BaseModel):
    responder = models.ForeignKey(Responder, on_delete=models.CASCADE, related_name='questionnaires', blank=True,
                                  null=True)
    interrogator = models.ForeignKey(Interrogator, on_delete=models.CASCADE, related_name='questionnaires', null=True,
                                     blank=True)


class Question(BaseModel):
    ANSWER = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, null=True)
    creator = models.ForeignKey(Interrogator, on_delete=models.CASCADE, null=True, blank=True)
    question_text = models.TextField()
    answer = models.CharField(max_length=3, choices=ANSWER, blank=True, null=True)

    def __str__(self):
        return self.question_text


class SubQuestion(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    creator = models.ForeignKey(Interrogator, on_delete=models.CASCADE, null=True, blank=True)
    question_text = models.TextField()

    def __str__(self):
        return self.question_text


class SubQuestionAnswer(BaseModel):
    creator = models.ForeignKey(Interrogator, on_delete=models.CASCADE, null=True, blank=True)
    sub_question = models.ForeignKey(SubQuestion, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(max_length=255)
    is_marked = models.BooleanField(default=False)


class ResultQuestionnaire(BaseModel):
    responder = models.ForeignKey(Responder, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    question_answer = models.CharField(max_length=3)
    sub_question = models.ForeignKey(SubQuestion, on_delete=models.CASCADE)
    sub_question_answers = models.ManyToManyField(SubQuestionAnswer)
