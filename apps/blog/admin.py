from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Post, Category



class PostAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""
    text = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'

# class LikeInline(admin.TabularInline):
#     """Отзывы на странице фильма"""
#     model = Like


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	"""docstring for PostAdmin"""
	list_display = ('id', 'name', 'url')
	list_display_links = ('name',)
	search_fields = ('name',)
	save_as = True

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	# fieldsets = [
	# 	# (None, {'fields': ['title', 'intro', 'text']}),
	# 	('Post title', {'fields': ['title']}),
	# 	('Post intro', {'fields': ['intro']}),
	# 	('Post text', {'fields': ['text']}),
	# 	('Post draft', {'fields': ['draft']}),
	# 	('Date information', {'fields': ['date']}),
	# ]
	"""docstring for PostAdmin"""
	list_display = ('id', 'title', 'draft', 'date')
	list_display_links = ('title',)
	list_filter = ('date', 'draft')
	list_editable = ('draft',)
	search_fields = ('title',)
	save_as = True
	readonly_fields = ('date',)
	# inlines = [LikeInline]
	form = PostAdminForm

admin.site.site_title='mirsaid.uz'
admin.site.site_header='mirsaid.uz'
# admin.site.index_title='mirsaid.uz'
