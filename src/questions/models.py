from django.db import models

# Create your models here

class Quiz_question(models.Model):
	question=models.CharField(max_length=900,default='0000000')
	choice_1=models.CharField(max_length=200, default='0000000')
	choice_2=models.CharField(max_length=200, default='0000000')
	choice_3=models.CharField(max_length=200, default='0000000')
	choice_4=models.CharField(max_length=200, default='0000000')
