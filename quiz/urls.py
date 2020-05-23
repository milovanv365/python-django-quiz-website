from django.urls import path
from .views import IndexView, QuizStepOneView, QuizStepTwoView, QuizStepThreeView, QuizStepFourView, QuizStepFiveView,\
    QuizSendView

app_name = 'quiz'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('quiz/step_one', QuizStepOneView.as_view(), name='quiz_step_one'),
    path('quiz/step_two', QuizStepTwoView.as_view(), name='quiz_step_two'),
    path('quiz/step_three', QuizStepThreeView.as_view(), name='quiz_step_three'),
    path('quiz/step_four', QuizStepFourView.as_view(), name='quiz_step_four'),
    path('quiz/step_five', QuizStepFiveView.as_view(), name='quiz_step_five'),

    path('quiz/api/send', QuizSendView.as_view(), name='quiz_send')
]
