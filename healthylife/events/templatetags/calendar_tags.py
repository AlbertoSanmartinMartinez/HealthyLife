#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from django import template

register = template.Library()

@register.simple_tag
def get():
    pass
