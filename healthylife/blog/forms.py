#!/usr/local/bin/python
# coding: utf-8

from django import forms
from blog import models as blog_models

# Blog forms
class PostForm(forms.ModelForm):
    class Meta:
        model = blog_models.Post
        fields = []


class CommentFormAuthenticated(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'id': 'comment_title', 'placeholder':'Título del comentario'}))
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'id': 'comment_content', 'placeholder':'Contenido del comentario'}))

    class Meta:
        model = blog_models.Comment
        fields = ['title', 'content']

class CommentFormNotAuthenticated(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'id': 'comment_email', 'placeholder': 'Eamil'}))
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'id': 'comment_title', 'placeholder':'Título del comentario'}))
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'id': 'comment_content', 'placeholder':'Contenido del comentario'}))

    class Meta:
        model = blog_models.Comment
        fields = ['title', 'content', 'email']
