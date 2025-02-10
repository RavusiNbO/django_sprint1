from django.urls import path

from . import views

app_name = "blog"
p_name = "category/<slug:category_slug>/"
urlpatterns = [
    path("", views.index, name="index"),
    path("posts/<int:pk>/", views.post_detail, name="post_detail"),
    path(p_name, views.category_posts, name="category_posts"),
]
