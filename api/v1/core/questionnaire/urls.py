from django.urls import path
from . import views

urlpatterns = [
    # Заполнить анкету
    path('fill/', views.QuestionnaireFillView.as_view()),
]