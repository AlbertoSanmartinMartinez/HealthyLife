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
class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        write_only_fields = ('password')
        read_only_fields = ('id')

    def create(self, data):
        user = User.objects.create(
            username = data['username'],
            password1 = data['password1'],
            password2 = data['password2'],
            email = data['email'])
        user.set_password(data['password'])
        user.save()

        return user


class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

    def authenticate(self, data):
        user = User.objects.authenticate(
            username=data['username'],
            password=data['password'])

        return user
"""

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        field = ('username', 'mail', 'password')


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.UserProfile
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
