from django.shortcuts import render
from questions.forms import Createquiz_form
from crquiz.forms import Title_form
from questions.models import Quiz_question
from crquiz.models import Create_quiz
from django.http import HttpResponse, HttpResponseRedirect
import random


# Create your views here.

def home_view(request):	
	return render(request, "quiz_pg.html",{})

def createquiz_view(request):
	if request.method=='POST':
		form1=Title_form(request.POST)
		if form1.is_valid():
			saved_form=form1.save()
			saved_form.unique_id=random.randint(1,1000)
			form1.save()
			return HttpResponseRedirect('/createquiz/question/')
		form1=Title_form()
	return render(request,"createquiz.html",{'title_form':form1})
	

def takequiz_view(request):
	return render(request,"takequiz.html",{})

def question_view(request):
	if request.method=='POST':
		form=Createquiz_form(request.POST)
		if form.is_valid():
			form.save()
	form = Createquiz_form()
	return render(request,"question.html",{'question_form':form})