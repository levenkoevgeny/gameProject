from rest_framework import serializers
from .models import Answer, Question


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'game',
                  'character',
                  'is_first_question_in_game', 'question_text', 'question_number',
                  'question_img', 'question_img_description', 'answers']
        depth = 2
