import json

from django.db.models import F
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.models import Questionnaire, Question, Responder, ResultQuestionnaire, SubQuestionAnswer


class ResponderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responder
        fields = (
            'id',
            'birth_date',
            'gender',
        )


class ResultQuestionnaireSerializer(serializers.ModelSerializer):
    sub_question_answers = serializers.PrimaryKeyRelatedField(queryset=SubQuestionAnswer.objects.all(), many=True)

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


class QuestionnaireFillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = (
            'id',
            'interrogator',
            'responder',
        )

    def to_internal_value(self, data):
        responder_birth_date = data.pop('birth_date', '')
        responder_gender = data.pop('gender', '')
        questionnaire = data.pop('questionnaire', [])
        response = super().to_internal_value(data)
        if responder_birth_date and responder_gender:
            responder_data = dict(birth_date=responder_birth_date, gender=responder_gender)
            serializer = ResponderSerializer(data=responder_data)
            serializer.is_valid(raise_exception=True)
            response['responder'] = serializer.save()
        else:
            raise ValidationError({"detail": "Data does not exists"})
        if questionnaire:
            for question in questionnaire:
                result_data = dict(responder=response['responder'].id, question=question['question']['id'],
                                   question_answer=question['question']['answer'],
                                   sub_question=question['question']['sub_question']['id'],
                                   sub_question_answers=question['question']['sub_question']['answers'])
                serializer = ResultQuestionnaireSerializer(data=result_data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
        else:
            raise ValidationError({"detail": "Data does not exists"})
        return response
