# from django.contrib import admin
from django.urls import path
from blog.views import BlogView, detailViewPost, CategoriesView, ApiView


urlpatterns = [
    path('', BlogView.as_view()),
    path("<str:url>/", CategoriesView.as_view(), name="category_url"),
    path("<str:category_url>/<slug:url>/", detailViewPost),

    # path("review/<int:pk>/", AddReview.as_view(), name="add_review"),
    # path('admin/<str:first_name>/', admin.site.urls, name="admin"),
]
