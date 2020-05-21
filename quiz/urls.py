from django.urls import path
from .views import IndexView, QuizStepOneView

app_name = 'quiz'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('quiz/step_one', QuizStepOneView.as_view(), name='quiz_step_one')
]
