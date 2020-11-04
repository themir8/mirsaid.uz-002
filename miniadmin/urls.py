from django.urls import path
from .views import AdminView, postEditView, deletePost, CreatePost, DrafterPost


urlpatterns = [
    path('', AdminView.as_view(), name="index"),
    path('new-post', CreatePost, name="index"),
    path("edit/<str:category_url>/<int:pk>/", postEditView),
    path("drafter/<str:category_url>/<int:pk>/", DrafterPost),
    path("delete/<str:category_url>/<int:pk>/", deletePost),
]
