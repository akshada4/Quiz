# Generated by Django 3.0.8 on 2020-08-02 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crquiz', '0003_remove_create_quiz_quiz_question'),
        ('questions', '0002_auto_20200802_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz_question',
            name='create_quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crquiz.Create_quiz'),
        ),
    ]
