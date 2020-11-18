from django.contrib import admin
from django.urls import path, include
from main.views import Registration, LoginView

urlpatterns = [
    path('', include('main.urls')),
    path('blog/', include('blog.urls')),
    path('course/', include('school.urls')),
    path('admin/', admin.site.urls, name='admin_panel'),
    path('mini-admin/', include('miniadmin.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path("ApiView/<int:pk>/", ApiView),
    path("signup/", Registration),
    path("login/", LoginView),
]
