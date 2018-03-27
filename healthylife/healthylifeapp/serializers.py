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
http://blog.enriqueoriol.com/2015/03/django-rest-framework-serializers.html
"""
class UserSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(
        view_name = 'api:user-detail',
    )

    class Meta:
        model = User
        fields = ('uri', 'username', 'email', 'id')


class UserProfileSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('bio', 'phone')


# Blog Serializers
class CategorySerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(
        view_name='api:category-detail',
    )

    class Meta:
        model = models.Category
        fields = ('uri', 'name', 'description')


class PostSerializer(HyperlinkedModelSerializer):

    uri = HyperlinkedIdentityField(
        view_name= 'api:post-detail',
    )
    category = fields.CharField(read_only=True)
    author = fields.CharField(read_only=True)

    class Meta:
        model = models.Post
        fields = ('uri', 'id', 'status', 'category', 'author', 'title', 'description', 'content', 'creation_date')



class CommentSerializer(HyperlinkedModelSerializer):
    """clase para serializar el modelo comentario"""
    uri = HyperlinkedIdentityField(
        view_name = 'api:comment-detail',
    )
    author_id = fields.CharField(read_only=True)
    post_id = fields.CharField(read_only=True)

    class Meta:
        model = models.Comment
        fields = ('uri', 'status', 'title', 'content', 'author_id', 'post_id')


# Shop serializers
