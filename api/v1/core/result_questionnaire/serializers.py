from rest_framework import serializers

from core.models import ResultQuestionnaire


class ResultCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultQuestionnaire
        fields = (
            'id',
            'responder',
            'question',
            'question_answer',
            'sub_question',
            'sub_question_answers'
        )