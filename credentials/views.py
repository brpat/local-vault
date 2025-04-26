from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def base(request):
    return render(request, 'templates/base.html')  # Simple reference 

def index(request):
    app_title:str = "Local Vault"
    template = loader.get_template('templates/index.html')
    context = {
        'app_title': app_title,
    }
    return HttpResponse(template.render(context, request))  # dynamic variable rendering


def login(request):
    template = loader.get_template("templates/login.html")
    context = {}
    
    return HttpResponse(template.render(context, request))


def signup(request):
    template = loader.get_template("templates/signup.html")
    context = {}
    
    return HttpResponse(template.render(context, request))