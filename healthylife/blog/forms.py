#!/usr/local/bin/python
# coding: utf-8

from django import forms
from blog import models as blog_models

# Blog forms
class PostForm(forms.ModelForm):
    class Meta:
        model = blog_models.Post
        fields = []


class PostFilter(forms.ModelForm):
    title = forms.CharField(label='Título', required=False, widget=forms.TextInput(attrs={'placeholder':'Escribe lo que quieras'}))
    minimum_date = forms.DateField(label='fecha mínima', required=False, widget=forms.DateInput(attrs={'placeholder': 'Mínimo'}))
    maximum_date = forms.DateField(label='fecha máxima', required=False, widget=forms.DateInput(attrs={'placeholder': 'Máximo'}))
    ORDER_BY = ((1, ("Más antiguos primero")), (2, ("Más recientes primero")))
    order_by = forms.ChoiceField(choices = ORDER_BY, label="Ordenar", initial=1, widget=forms.Select(), required=False)

    def __init__(self, *args, **kwargs):
        super(PostFilter, self).__init__(*args, **kwargs)
        self.fields['category'] = forms.ModelChoiceField(
            label='Categoria',
            required=False,
            queryset=blog_models.Category.objects.all())

    class Meta:
        model = blog_models.Post
        exclude = ['description', 'content']


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = blog_models.Comment
        fields = '__all__'


class CommentFormAuthenticated(forms.Form):
    title = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'id': 'comment_title', 'placeholder':'Título del comentario'}))
    content = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'id': 'comment_content', 'placeholder':'Contenido del comentario'}))

    """
    class Meta:
        model = blog_models.Comment
        fields = ['title', 'content']
    """

class CommentFormNotAuthenticated(forms.Form):
    name = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'id': 'comment_title', 'placeholder':'Nombre'}))
    email = forms.EmailField(label='', required=False, widget=forms.EmailInput(attrs={'id': 'comment_email', 'placeholder': 'Email'}))
    title = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'id': 'comment_title', 'placeholder':'Título del comentario'}))
    content = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'id': 'comment_content', 'placeholder':'Contenido del comentario'}))

    """
    class Meta:
        model = blog_models.Comment
        fields = ['name', 'title', 'content', 'email']
    """





    #
