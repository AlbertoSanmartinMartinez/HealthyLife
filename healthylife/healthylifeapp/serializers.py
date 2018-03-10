#!/usr/local/bin/python
# coding: utf-8

from rest_framework import serializers
from healthylifeapp import models
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from django.contrib.auth.models import User
from rest_framework import fields

# General Serializers
"""
class UserSerializer(serializers.HyperlinkedIdentityField):
    uri = HyperlinkedIdentityField(
        view_name= 'api:user-detail',
    )

    class Meta:
        model = User
        fields = ('username', 'email')
"""

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.CustomUser
        fields = ('bio', 'phone')


# Blog Serializers
class PostSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(
        view_name= 'api:post-detail',
    )
    category = HyperlinkedRelatedField(
        view_name = 'api:category-detail',
        read_only = True,
    )
    author = fields.CharField(read_only=True)

    class Meta:
        model = models.Post
        fields = ('uri', 'status', 'title', 'description', 'content', 'category', 'author')


class CommentSerializer(HyperlinkedModelSerializer):
    """clase para serializar el modelo comentario"""
    uri = HyperlinkedIdentityField(
        view_name = 'api:comment-detail',
    )
    author = fields.CharField(read_only=True)
    post = HyperlinkedRelatedField(
        view_name='api:post-detail',
        read_only=True,
    )

    class Meta:
        model = models.Comment
        fields = ('uri', 'status', 'title', 'content', 'author', 'post')


class CategorySerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(
        view_name='api:category-detail',
    )

    class Meta:
        model = models.Category
        fields = ('uri', 'name', 'description')


# Shop serializers
