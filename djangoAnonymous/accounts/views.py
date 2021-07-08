 
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.


def register(request):

    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # form.save()
            #log user in
            user = form.save()
            login(request,user)
            return render(request,'registration/signup_success.html')
    else:
        form = RegisterForm()
            
    return render(request, 'registration/signup.html', {
        'form': form
    })
    # else:

def login_view(request,user_id):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user(id=user_id)
            login(request,user)
            return render(request, 'index.html')

    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html',{
        'form':form
    })


def logout_view(request):
    if request.method == 'POST':
        logout(request)

        return redirect('accounts:login')