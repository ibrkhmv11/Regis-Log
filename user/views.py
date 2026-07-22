from django.shortcuts import render , redirect
from django.views import View

from user.forms import RegisterForm

def home(request):
    return render(request,'home.html')

class RegisterView(View):
    def get(self,request):
        form = RegisterForm()
        return render(request,'register.html',{'form':form})

    def post(self,request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('home')
        return render(request,'register.html',{'form':form})

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from .forms import LoginForm

class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if not user:

                form.add_error(None, 'Username yoki parol xato.')
                return render(request, 'login.html', {'form': form})

            login(request, user)
            return redirect('home')

        return render(request, 'login.html', {'form': form})