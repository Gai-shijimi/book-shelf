from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm
from .models import ReadBook

from django import forms


class ReadBookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '入力必須(40文字以下)'
    }))

    consideration4 = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': '入力必須、50文字以上入力してください。'})
    )

    class Meta:
        model = ReadBook
        fields = [
            'title',
            'quote1', 'consideration1',
            'quote2', 'consideration2',
            'quote3', 'consideration3',
            'consideration4', 'category',
        ]


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email',)
