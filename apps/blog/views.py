from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .models import Post, Category



class BlogView(ListView):
    """Основная страница"""

    model = Post
    # Филтруеть посты если пост не черновык то выведёт пост
    queryset = Post.objects.filter(draft=False).order_by('-date')

    # paginate_by = 1
    paginate_by = 3

def detailViewPost(request, category_url, url):
    """Подробный просмотр поста"""

	# получает обект
    post = Post.objects.get(url=url)

    return render(request, 'blog/post.html',
        {'el': post,
		'title': 'Подробный просмотр поста',
        'nav_name': post.title})

    if request.method == 'POST':
        review = Reviews(
            email=request.POST['email'],
            name=request.POST['name'],
            text=request.POST['text']
            )
        review.save()

        return redirect(post.get_absolute_url)

class CategoriesView(View):
    def get(self, request, url):
        # получает обект
        query = Category.objects.filter(url=url)

        return render(request, 'blog/category.html',
        {'query': query})

def ApiView(request, pk):

    queryset = dict(Post.objects.filter(pk=pk))

    return JsonResponse(queryset)