from django.shortcuts import render

# Create your views here.
import json
import psycopg
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from .forms import SignUpForm



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
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        print(f"Username: {username}, Password: {password}")
        from .models import Vault_User
        try:
            user = Vault_User.objects.get(username=username)
            if user.check_password(password):
                # Successful login
                template = loader.get_template("templates/myvault.html")
                context = {'user_name': user.user_first_name}
                return HttpResponse(template.render(context, request))
            else:
                error = "Invalid username or password."
        except Vault_User.DoesNotExist:
            error = "Invalid username or password."
        template = loader.get_template("templates/login.html")
        context = {'error': error}
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("templates/login.html")
        context = {}
        return HttpResponse(template.render(context, request))


def signup(request):
    template = loader.get_template("templates/signup.html")
    context = {}
    
    return HttpResponse(template.render(context, request))

@csrf_protect
def postsignup(request):
    if request.method == "POST":
        # Access form data using request.POST
        form = SignUpForm(request.POST)
        print(form.errors)

        if form.is_valid():
            print("Form is valid")
            # first_name = request.POST.get('first_name')
            # last_name = request.POST.get('last_name')
            # username = request.POST.get('username')
            # password = request.POST.get('password')
            # password_repeat = request.POST.get('password_repeat')

            user = form.save()  # Save the user data
        else:
            return HttpResponse("Invalid form input")


        # Debugging: Print the form data
        # print(f"First Name: {first_name}, Last Name: {last_name}, Username: {username}")
        # print(f"Password: {password}, Password Repeat: {password_repeat}")

        # Add your logic here (e.g., save to database, validate passwords, etc.)
        # context = {
        #     'first_name': first_name,
        #     'last_name': last_name,
        #     'username': username,
        # }
        context = {}
        template = loader.get_template("templates/postsignup.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("Invalid request method")
    

def myvault(request):
    template = loader.get_template("templates/myvault.html")
    context = {
         'user_name': 'Brijesh',
    }
    
    return HttpResponse(template.render(context, request))