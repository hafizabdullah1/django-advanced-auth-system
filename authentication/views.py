from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "home.html")

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid usuername.")
            return redirect('login')

        user = authenticate(username = username, password = password)
        
        if user is None:
            messages.error(request, "Invalid password.")
            return redirect('login')
        else:
            login(request, user)
            return redirect('welcome')
    
    return render(request, 'login.html')


def registerPage(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.info(request, "Username already taken.")
            return redirect('register')
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )
        
        user.set_password(password)
        user.save()
        messages.info(request, "Account created Successfully.")
        
        return redirect('login')
    
    return render(request, 'register.html')


def logout_page(request):
    logout(request)
    return redirect('login')

@login_required(login_url="/login")
def welcome_page(request):
    return render(request, "welcome.html")