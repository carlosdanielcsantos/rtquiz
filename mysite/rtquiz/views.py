from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Quiz, Question, Answer


class IndexView(generic.ListView):
    model = Quiz
    template_name = 'rtquiz/index.html'


class QuizView(generic.ListView):
    model = Question
    template_name = 'rtquiz/detail.html'


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'rtquiz/results.html', {'question': question})


def reply(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    answer = Answer(question_id=question.id,
                    answer_text=request.POST['answer_text'],
                    author='me')
    answer.save()
    return HttpResponse(status=204)
