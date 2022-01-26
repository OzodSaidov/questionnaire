from rest_framework import generics
from rest_framework.permissions import AllowAny

from api.v1.core.questionnaire.serializers import QuestionnaireFillSerializer


class QuestionnaireFillView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = QuestionnaireFillSerializer
