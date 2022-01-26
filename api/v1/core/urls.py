from django.urls import path, include


urlpatterns = [
    path('questionnaire/', include('api.v1.core.questionnaire.urls')),
    path('question/', include('api.v1.core.question.urls')),
    path('result_questionnaire/', include('api.v1.core.result_questionnaire.urls'))
]