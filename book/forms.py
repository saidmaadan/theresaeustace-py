from django import forms
from .models import ReviewRating

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['user_name', 'user_email', 'subject', 'review', 'rating']