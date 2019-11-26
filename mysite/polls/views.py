# -*- coding: utf-8 -*-
"""
:Authors: norlyakov
:Date: 23.11.2019
"""
from django.utils import timezone
from rest_framework import viewsets

from .models import Question
from .serializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    serializer_class = QuestionSerializer
