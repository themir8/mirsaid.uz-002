from django.forms import ModelForm
from blog.models import Post, Category


class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['image', 'title', 'intro', 'text', 'url', 'draft', 'author', 'category', 'date']