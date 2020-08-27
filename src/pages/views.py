from django.shortcuts import render
from questions.forms import Createquiz_form
from crquiz.forms import Title_form
from questions.models import Quiz_question
from crquiz.models import Create_quiz
from takequiz.forms import Search_form
from django.http import HttpResponse, HttpResponseRedirect
from takequiz.models import Take_quiz
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
	

def search_view(request):
	form=Search_form()
	query=None
	if request.method=='GET':
		searched = request.GET.get('search')
		query = Create_quiz.objects.filter(title=searched)	
		id_query = request.GET.get('id')	
		if id_query != None:
			return render(request, "quiz.html", {'quiz':Quiz_question.objects.filter(create_quiz=id_query)})
	return render(request,"search.html",{'search_form':form, 'query':query})

def question_view(request):
	if request.method=='POST':
		form=Createquiz_form(request.POST)
		if form.is_valid():
				saved_form=form.save(commit=False)
				saved_form.create_quiz=Create_quiz.objects.filter(id=title_id)
				form.save()
	form = Createquiz_form()
	return render(request,"question.html",{'question_form':form})
