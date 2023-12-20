from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def signupmod(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'loginmod.html', {'success': "Registration successful. Please login."})
        else:
            error_message = form.errors.as_text()
            return render(request, 'signupmod.html', {'error': error_message})

    return render(request, 'signupmod.html')

def loginmod(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dashboard")
        else:
            return render(request, 'loginmod.html', {'error': "Invalid credentials. Please try again."})

    return render(request, 'loginmod.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'name': request.user.first_name})

@login_required
def vidi(request):
    return render(request, 'vidi.html', {'name': request.user.first_name + " " + request.user.last_name})

@login_required
def logoutmod(request):
    logout(request)
    return redirect("/loginmod")

@login_required
def room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/vidi?roomID=" + roomID)
    return render(request, 'room.html')





