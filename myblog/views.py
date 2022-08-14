from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
#from .templates import base.html

#def home(request):
#    html = '<html><body>женя совершенное создание, а я бесполезный еблан</body></html>'
#    return HttpResponse(html)

def home(request):
    return render(request, 'base.html')