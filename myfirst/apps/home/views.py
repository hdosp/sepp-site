from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def index(request):
	return render(request, 'home/index.html')

def people(request):
	return render(request, 'home/people.html')
