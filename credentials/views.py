from django.shortcuts import render, redirect

# Create your views here.
import json
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
        from .models import Vault_User
        try:
            user = Vault_User.objects.get(username=username)
            if user.check_password(password):
                # Save username in session for authentication
                request.session['username'] = user.username
                template = loader.get_template("templates/myvault.html")
                return redirect('myvault')
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

@csrf_protect
def add_credential(request):
    if request.method == "POST":
        cred_name = request.POST.get('cred_name')
        cred_website = request.POST.get('cred_website')
        cred_username = request.POST.get('cred_username')
        cred_password = request.POST.get('cred_password')
        cred_notes = request.POST.get('cred_notes')

        # Assume user is authenticated and username is in session
        username = request.session.get('username')
        if not username:
            return HttpResponse("User not authenticated", status=401)

        from django.db import connection
        table_name = f"credential_{username}"
        create_table_sql = f'''
        CREATE TABLE IF NOT EXISTS "{table_name}" (
            name TEXT PRIMARY KEY,
            website TEXT,
            username TEXT,
            password TEXT,
            notes TEXT
        );
        '''
        try:
            with connection.cursor() as cursor:
                cursor.execute(create_table_sql)
                cursor.execute(
                    f"INSERT INTO \"{table_name}\" (name, website, username, password, notes) VALUES (%s, %s, %s, %s, %s)",
                    [cred_name, cred_website, cred_username, cred_password, cred_notes]
                )
            connection.commit()  # Explicitly commit the transaction
            return HttpResponse("Credential added successfully!")
        except Exception as e:
            return HttpResponse(f"Error adding credential: {str(e)}", status=500)

def myvault(request):
    username = request.session.get('username', '')
    print(f"Username from session: {username}")
    credentials = []
    if username:
        from django.db import connection
        table_name = f"credential_{username}"
        try:
            with connection.cursor() as cursor:
                cursor.execute(f'SELECT name, website, username, password, notes FROM "{table_name}"')
                rows = cursor.fetchall()
                for row in rows:
                    credentials.append({
                        'name': row[0],
                        'website': row[1],
                        'username': row[2],
                        'password': row[3],
                        'notes': row[4],
                    })
                    print(row)
        except Exception:
            pass  # Table may not exist yet, or no credentials
    template = loader.get_template("templates/myvault.html")
    context = {
         'user_name': username,
         'credentials': credentials,
    }
    return HttpResponse(template.render(context, request))

def logout(request):
    request.session.flush()  # Clear all session data
    return redirect('login')