from django.urls import path
from . import views

urlpatterns = [
    path('fill/', views.QuestionnaireFillView.as_view()),
]