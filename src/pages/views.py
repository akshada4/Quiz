from django.shortcuts import render
from questions.forms import Createquiz_form
from crquiz.forms import Title_form
from questions.models import Quiz_question
from crquiz.models import Create_quiz
from django.http import HttpResponse, HttpResponseRedirect
import random


# Create your views here.
title_id=0

def home_view(request):	
	return render(request, "quiz_pg.html",{})

def createquiz_view(request):
	global title_id
	if request.method=='POST':
		form1=Title_form(request.POST)
		if form1.is_valid():
			saved_form=form1.save()	
			title_id=saved_form.id
			return HttpResponseRedirect('/createquiz/question/')
		form1=Title_form()
	return render(request,"createquiz.html",{'title_form':form1})
	

def takequiz_view(request):
	return render(request,"takequiz.html",{})

def question_view(request):
	if request.method=='POST':
		form=Createquiz_form(request.POST)
		if form.is_valid():
				saved_form=form.save(commit=False)
				saved_form.create_quiz=Create_quiz.objects.get(id=title_id)
				form.save()
	form = Createquiz_form()
	return render(request,"question.html",{'question_form':form})