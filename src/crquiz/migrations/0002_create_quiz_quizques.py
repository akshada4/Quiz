# Generated by Django 3.0.8 on 2020-07-29 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20200729_1312'),
        ('crquiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_quiz',
            name='quizques',
            field=models.ForeignKey(default='0000000', on_delete=django.db.models.deletion.CASCADE, to='questions.Quiz_question'),
        ),
    ]