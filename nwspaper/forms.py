from django import forms
# from django.forms import ModelForm
from .models import Post, Author, Category
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
#    author = forms.ModelChoiceField(queryset=Author.objects.all(), label='Автор')
#    category = forms.ModelChoiceField(queryset=Category.objects.all, label='Категория')
    title = forms.CharField(label='Заголовок', max_length=128)
    text = forms.CharField(label='Текст', min_length=20, widget=forms.Textarea)

    class Meta:
        model = Post
        fields = [
           'author',
           'post_category',
           'title',
           'text',
           'rating',

           ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        if title == text:
            raise ValidationError(
                "Заголовок не должен быть идентичен тексту."
            )

        return cleaned_data

