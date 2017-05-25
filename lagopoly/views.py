from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView


def home(request):
	return render(request, 'home.html')

def faqs(request):
	return render(request, 'faqs.html')

def privacy(request):
	return render(request, 'privacy.html')

def termsofuse(request):
	return render(request, 'termsofuse.html')


class HelloWorldView(View):
	def get(self, request):
		return HttpResponse("Hello World!")


class HomeView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["games_today"] = 6
		return context