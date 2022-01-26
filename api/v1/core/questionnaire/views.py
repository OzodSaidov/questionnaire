from rest_framework import generics
from rest_framework.permissions import AllowAny

from api.v1.core.questionnaire.serializers import QuestionnaireFillSerializer
from core.models import Questionnaire


class QuestionnaireFillView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    # queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireFillSerializer


# class QuestionnaireRetrieveView(generics.RetrieveAPIView):
#     permission_classes = [AllowAny]
#     queryset = Questionnaire.objects.all()
#     serializer_class = QuestionnaireRetrieveSerializer
