from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class CN4View(TemplateView):
	template_name = 'c4.html'