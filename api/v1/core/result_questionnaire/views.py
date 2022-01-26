from rest_framework import generics
from rest_framework.permissions import AllowAny

from api.v1.core.result_questionnaire.serializers import ResultCreateSerializer


class ResultCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResultCreateSerializer
