#!/usr/local/bin/python
# coding: utf-8

from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from blog import models as blog_models
from rest_framework import fields

# Blog Serializers
class CategorySerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(
        view_name='api:category-detail',
    )

    class Meta:
        model = blog_models.Category
        fields = ('uri', 'name', 'description')


class PostSerializer(HyperlinkedModelSerializer):

    uri = HyperlinkedIdentityField(
        view_name= 'api:post-detail',
    )
    category = fields.CharField(read_only=True)
    author = fields.CharField(read_only=True)

    class Meta:
        model = blog_models.Post
        fields = ('uri', 'id', 'status', 'category', 'author', 'title', 'description', 'content', 'creation_date')



class CommentSerializer(HyperlinkedModelSerializer):
    """clase para serializar el modelo comentario"""
    uri = HyperlinkedIdentityField(
        view_name = 'api:comment-detail',
    )
    author_id = fields.CharField(read_only=True)
    post_id = fields.CharField(read_only=True)

    class Meta:
        model = blog_models.Comment
        fields = ('uri', 'status', 'title', 'content', 'author_id', 'post_id')
