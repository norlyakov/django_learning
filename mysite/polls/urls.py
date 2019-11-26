# -*- coding: utf-8 -*-
"""
:Authors: norlyakov
:Date: 23.11.2019
"""
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('questions', views.QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
