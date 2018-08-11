from django.urls import path
from . import views

app_name = 'rtquiz'
urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('<int:pk>/', views.QuizView.as_view(), name='detail'),
        path('<int:question_id>/reply', views.reply, name='reply'),
        ]

