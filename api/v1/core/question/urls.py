from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.QuestionListView.as_view()),
    path('<int:pk>/subquestion/', views.SubQuestionRetrieveView.as_view()),
]