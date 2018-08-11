from django.db import models
from django.utils import timezone

import datetime


class Quiz(models.Model):
    name = models.CharField(max_length=100)
    creation_date = models.DateTimeField()

    def was_published_recently(self):
        return self.creation_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.TextField()
    answerable = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return "=====\n + " + \
               "author: " + self.author + \
               "-----\n" + self.answer_text
