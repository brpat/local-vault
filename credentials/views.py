from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
    app_title:str = "Local Vault"
    template = loader.get_template('templates/index.html')
    context = {
        'app_title': app_title,
    }
    return HttpResponse(template.render(context, request))