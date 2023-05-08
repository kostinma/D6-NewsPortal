from django.shortcuts import render

from datetime import datetime
from pprint import pprint

from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    # ordering = 'title'
    ordering = 'time_in'
    # Or, alternatively
    # queryset = Post.objects.order_by('time_in')
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        # pprint(context)
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

# End of file
