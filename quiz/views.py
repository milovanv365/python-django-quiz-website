from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    template_url = 'index.html'

    def get(self, request):
        return render(request, template_name=self.template_url)


class QuizStepOneView(View):
    template_url = 'quiz_step_one.html'

    def get(self, request):
        return render(request, template_name=self.template_url)


class QuizStepTwoView(View):
    template_url = 'quiz_step_two.html'

    def get(self, request):
        context = {

        }
        return render(request, template_name=self.template_url, context=context)
