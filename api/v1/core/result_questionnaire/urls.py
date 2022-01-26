from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.ResultCreateView.as_view())
]