from django.db import models
from questions.models import Quiz_question

# Create your models here.
class Create_quiz(models.Model):
	title=models.CharField(max_length=900,default='0000000')
	unique_id=models.IntegerField(default=0)
	quizques=models.ManyToManyField(Quiz_question)


	