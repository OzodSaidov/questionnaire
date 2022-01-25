from django.db import models
from django.contrib.auth.models import AbstractUser
from config.base_models import BaseModel


class User(AbstractUser):
    ADMIN = 1
    INTERROGATOR = 2
    ROLE = (
        (ADMIN, 'Admin'),
        (INTERROGATOR, 'Interrogator')
    )
    role = models.IntegerField(choices=ROLE, default=2)

    @property
    def get_full_name(self):
        return super(User, self).get_full_name()

    def __str__(self):
        return self.username
