from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    template_url = 'index.html'

    def get(self, request):
        return render(request, template_name=self.template_url)
