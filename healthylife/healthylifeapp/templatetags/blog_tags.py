#!/usr/local/bin/python
# coding: utf-8

from django import template
from django.shortcuts import render

register = template.Library()

@register.filter('comment_answers')
def comment_answers():
    comment_answers = models.Comment.objects.filter(parent_id=7).order_by("-creation_date")

    return recomment_answers if comment_answers else None

#register.filter('comment_answers', comment_answers)
