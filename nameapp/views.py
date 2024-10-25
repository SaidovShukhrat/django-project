from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class myName(TemplateView):
    template_name = 'name.html'

class myLast(TemplateView):
    template_name = 'last.html'