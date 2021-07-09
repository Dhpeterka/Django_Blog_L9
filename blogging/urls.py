from django.urls import path
from blogging.views import stub_view, list_view, detail_view, new_post
from blogging.feeds import LatestPosts

urlpatterns = [
    path('', list_view, name='blog_index'),
    path('posts/<int:post_id>/', detail_view, name='blog_detail'),
    path('feed/rss/', LatestPosts(), name='post_feed'),
    path('blog/new/', new_post, name='new_post'),
]
