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


# Shop serializers
