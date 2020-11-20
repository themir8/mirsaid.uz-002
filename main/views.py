from django import forms
from django.shortcuts import render
from django.views.generic.base import View
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from blog.models import Post

class MainView(View):
    """Основная страница"""
    def get(self, request):

    	# Филтруеть посты если пост не черновык то выведёт пост
    	query = Post.objects.filter(draft=False).order_by('-date')[:3]

    	return render(request, 'main/index.html',
    		{'title': 'Основная страница',
            'nav_name': 'Основная страница',
            'post_list': query})


def Registration(request):
    print(request.user.is_authenticated)
    if(not request.user.is_authenticated):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                new_user = form.save()
                return HttpResponseRedirect("/")
        else:
            form = UserCreationForm()
        return render(request, "main/registration.html", {
            'form': form,
            })
    else:
       return HttpResponseRedirect("/") 


def LoginView(request):
    if(not request.user.is_authenticated):
        if request.method == "POST":
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            
            user = authenticate(
                username=username,
                password=password
                )
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect("/account/invalid/")
    else:
           return HttpResponseRedirect("/") 
    
    return render(request, 'main/login.html')

