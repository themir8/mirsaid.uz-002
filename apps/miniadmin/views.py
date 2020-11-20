from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

from blog.models import Post, Category
from .forms import PostForm


class AdminView(View):
    """Основная страница"""
    def get(self, request):
            # Филтруеть посты по дате
            post = Post.objects.order_by('-date')
            category = Category.objects.order_by('-id')

            return render(request, 'miniadmin/index.html',
            	{'title': 'Основная страница',
                'nav_name': 'Основная страница',
                'post_list': post,
                'category_list': category})


@login_required
def postEditView(request, category_url, pk):
    
    post = Post.objects.get(id=pk)

    if request.method == "POST":
    	title = request.POST.get('title', '')
    	intro = request.POST.get('intro', '')
    	text = request.POST.get('text', '')
    	post.title = title
    	post.intro = intro
    	post.text = text
    	post.save()

    	try:
    		return HttpResponseRedirect("/mini-admin/")
    	except Exception as e:
    		return HttpResponse(str(e))

    return render(request, 'miniadmin/edit.html',
    	{'title': 'Основная страница',
        'nav_name': 'Основная страница',
        'post': post})
    

@login_required
def deletePost(request, category_url, pk):
    
    if request.method == 'GET':
        
        post = Post.objects.get(pk=pk)

        post.delete()

        return HttpResponseRedirect(request.path)
    # else:
    #     return HttpResponseRedirect("/blog/")


@login_required
def DrafterPost(request, category_url, pk):
    
    if request.method == 'GET':
        
        post = Post.objects.get(pk=pk)

        if post.draft:
            post.draft = False
        else:
            post.draft = True
        post.save()

        return HttpResponseRedirect("/")


def CreatePost(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/mini-admin/')
        else:
            return HttpResponse("error")
    else:
        form = PostForm()


    return render(request, 'miniadmin/create.html', {'form': form})
