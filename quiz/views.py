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
            'sales_values': sales_values,
            'commission_values': commission_values
        }
        return render(request, template_name=self.template_url, context=context)


class QuizStepThreeView(View):
    template_url = 'quiz_step_three.html'

    def get(self, request):
        distance_values = []
        for x in range(1000, 26000, 1000):
            distance_values.append(x)

        data_usage_values = []
        for x in range(1, 21, 1):
            data_usage_values.append(x)

        context = {
            'distance_values': distance_values,
            'data_usage_values': data_usage_values
        }
        return render(request, template_name=self.template_url, context=context)


class QuizStepFourView(View):
    template_url = 'quiz_step_four.html'

    def get(self, request):

        important_things = [
            {'value': 'a great work environment / good colleagues', 'label': 'et supert arbeidsmiljø/gode kolleger'},
            {'value': 'opportunity for personal development', 'label': 'mulighet for personlig utvikling'},
            {'value': 'the best technology', 'label': 'den beste teknologien'},
            {'value': 'opportunity for partnership', 'label': 'mulighet for partnerskap'},
            {'value': 'high salary', 'label': 'høy lønn'},
            {'value': 'freedom', 'label': 'frihet'},
            {'value': 'flexibility', 'label': 'fleksibilitet'},
            {'value': 'to be able to influence the workplace', 'label': 'å kunne påvirke arbeidsplassen'},
            {'value': 'quality', 'label': 'kvalitet'},
            {'value': 'safety', 'label': 'trygghet'},
            {'value': 'to have back office', 'label': 'å ha backoffice'},
            {'value': 'the best toolbox', 'label': 'den beste verktøykassen'},
            {'value': 'winning culture', 'label': 'vinnerkultur'},
            {'value': 'good lead approach', 'label': 'god leadstilgang'}
        ]

        context = {
            'important_things': important_things
        }

        return render(request, template_name=self.template_url, context=context)


class QuizStepFiveView(View):
    template_url = 'quiz_step_five.html'

    def get(self, request):
        return render(request, template_name=self.template_url)
