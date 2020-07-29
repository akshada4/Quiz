from django import forms
from .models import Create_quiz



class Title_form(forms.ModelForm):
	title=forms.CharField()
	class Meta:
		model=Create_quiz
		fields=[
			'title'
		]