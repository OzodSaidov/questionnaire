from django.db import models
from django.contrib.auth.models import User
from config.base_models import BaseModel


class Interrogator(BaseModel):
    """
    Опросчик
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def count_questionnaire(self) -> int:
        return self.questionnaires.filter(is_completed=True).count()
