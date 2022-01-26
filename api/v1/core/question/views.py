from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny

from api.v1.core.question.serializers import SubQuestionRetrieveSerializer, QuestionListSerializer
from core.models import SubQuestion, Question


class QuestionListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = QuestionListSerializer
    queryset = Question.objects.all()


class SubQuestionRetrieveView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = SubQuestionRetrieveSerializer
    queryset = SubQuestion.objects.all()

    def get_object(self):
        sub_question = get_object_or_404(queryset=SubQuestion.objects.all(), id=self.kwargs.get('pk'))
        return sub_question
