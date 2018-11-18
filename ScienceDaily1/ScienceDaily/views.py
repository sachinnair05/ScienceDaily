from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.template import loader

@csrf_exempt
def homepage(request):
    # return HttpResponse('homepage')
    return render(request,'homepage.html')

@csrf_exempt
def about(request):
    # return HttpResponse('about')
    return render(request,'about.html')
