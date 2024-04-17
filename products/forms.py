from django import forms
from .models import Posts


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = "__all__"
        exclude = ['user']

        labels = {
            'title' : '상품명',
            'content' : '상품 설명',
            'price' : '가격',
        }
