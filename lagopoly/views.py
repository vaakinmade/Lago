from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def faqs(request):
	return render(request, 'faqs.html')

def privacy(request):
	return render(request, 'privacy.html')

def termsofuse(request):
	return render(request, 'termsofuse.html')