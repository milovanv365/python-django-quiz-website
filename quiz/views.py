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
        sales_values = []
        for x in range(0, 155, 5):
            if x == 0:
                sales_values.append(1)
            else:
                sales_values.append(x)

        commission_values = []
        for x in range(1000, 100000, 2500):
            commission_values.append(x)

        context = {
            "sales_values": sales_values,
            "commission_values": commission_values
        }
        return render(request, template_name=self.template_url, context=context)


class QuizStepThreeView(View):
    template_url = 'quiz_step_three.html'

    def get(self, request):
        return render(request, template_name=self.template_url)


class QuizStepFourView(View):
    template_url = 'quiz_step_four.html'

    def get(self, request):
        return render(request, template_name=self.template_url)


class QuizStepFiveView(View):
    template_url = 'quiz_step_five.html'

    def get(self, request):
        return render(request, template_name=self.template_url)
