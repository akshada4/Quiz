from django import forms
from .models import Take_quiz

class Search_form(forms.ModelForm):
	search=forms.CharField()
	class Meta:
		model=Take_quiz
		fields=[
			'search'
		]