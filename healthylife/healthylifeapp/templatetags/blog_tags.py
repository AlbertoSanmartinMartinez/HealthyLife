#!/usr/local/bin/python
# coding: utf-8

from django import template
from django.shortcuts import render
from healthylifeapp import models

register = template.Library()

@register.simple_tag
def get_comment_answers(comment_parent):
    """
    Template tag method que busca las respuestas a un comentario
    """
    comment_answers = models.Comment.objects.filter(parent_id=comment_parent).order_by("-creation_date")

    return comment_answers if comment_answers else None


#register.filter('comment_answers', comment_answers)
