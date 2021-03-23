from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator


class Category(models.Model):
    """カテゴリー"""
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class ReadBook(models.Model):
    """読んだ本"""
    title = models.CharField(blank=False, null=False, max_length=40)
    quote1 = models.TextField(blank=True)
    consideration1 = models.TextField(blank=True)
    quote2 = models.TextField(blank=True)
    consideration2 = models.TextField(blank=True)
    quote3 = models.TextField(blank=True)
    consideration3 = models.TextField(blank=True)
    consideration4 = models.TextField(blank=False, null=False, validators=[MinLengthValidator(50)])
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
