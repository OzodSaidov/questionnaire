from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.QuestionListView.as_view()),

    # В этом эндпоинте можно получить вторичный вопрос по id первиным вопросам
    path('<int:pk>/subquestion/', views.SubQuestionRetrieveView.as_view()),
]