# -*- coding: utf-8 -*-
"""
:Authors: norlyakov
:Date: 23.11.2019
"""
from django.contrib import admin

from .models import Question

admin.site.register(Question)
