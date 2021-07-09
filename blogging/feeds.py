from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post

class LatestPosts(Feed):
    title = "Latest Blog Posts"
    link = "/postfeed/"
    description = "New/Updated Posts from Blog"

    def items(self):
        return Post.objects.order_by('-published')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return reverse('blog_detail', args=[item.pk])
