import json
import time

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.core.mail import EmailMessage
from django.template.loader import get_template


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
        for x in range(25, 155, 5):
            sales_values.append(x)

        commission_values = []
        for x in range(20000, 102500, 2500):
            if x == 0:
                commission_values.append(1000)
            else:
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


class QuizSendView(View):
    def post(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Content-Type'] = 'text/plain'

        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        phone = request.POST.get('phone', None)

        main_data = request.POST.get('main_data')
        main_data = json.loads(main_data)

        email_data = {
            'name': name,
            'email': email,
            'phone': phone,
            'main_data': main_data
        }

        try:
            subject = "W Eiendomsmegling - Megler"
            to_email = ['milovanv365@gmail.com']
            from_email = "noreply@megler.weiendomsmegling.no"
            message = get_template('email.html').render(email_data)
            msg = EmailMessage(subject, message, from_email, to_email)
            msg.content_subtype = 'html'
            msg.send()
            print('email has been sent')
        except IOError as e:
            return e

        response.write('success')

        return response
