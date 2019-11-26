# -*- coding: utf-8 -*-
"""
:Authors: norlyakov
:Date: 26.11.2019
"""
from rest_framework import serializers

from .models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['choice_text', 'votes']


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ['question_text', 'pub_date', 'choices']

    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)
        for choice_data in choices_data:
            Choice.objects.create(question=question, **choice_data)
        return question
