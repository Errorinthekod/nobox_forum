from django.urls import path
from .views import post_list, post_detail, add_comment, toggle_like, toggle_like_comment



urlpatterns = [
    path('', post_list, name='post-list'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/<int:post_id>/comment/', add_comment, name='add-comment'),
    path('like/post/<int:post_id>/', toggle_like, name='toggle-like'),
    path('like/comment/<int:comment_id>/', toggle_like_comment, name='toggle-like-comment'),
]
