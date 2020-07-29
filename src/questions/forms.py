from django import forms
from .models import Quiz_question



class Createquiz_form(forms.ModelForm):
	question=forms.CharField()
	choice_1=forms.CharField()
	choice_2=forms.CharField()
	choice_3=forms.CharField()
	choice_4=forms.CharField()
	class Meta:
		model  = Quiz_question
		fields = [
			'question',
			'choice_1',
			'choice_2',
			'choice_3',
			'choice_4'
		]

