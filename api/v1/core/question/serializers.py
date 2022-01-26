from rest_framework import serializers

from core.models import SubQuestion, SubQuestionAnswer, Question


class AnswerRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubQuestionAnswer
        fields = (
            'id',
            'answer_text',
        )


class SubQuestionRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubQuestion
        fields = (
            'id',
        )

    def to_representation(self, instance: SubQuestion):
        data = super().to_representation(instance)
        data['answers'] = AnswerRetrieveSerializer(instance.answers.all(), many=True).data
        return data


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'question_text',
        )