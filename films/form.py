from django import forms
from .models import Reviews

class ReviewForm(forms.ModelForm):
    '''форма отзывов'''
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text_reviews')