from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'Homepage.html')
    # return HttpResponse('Home Page')

def about(request):
    return render(request, 'About.html')
    # return HttpResponse('About Page')