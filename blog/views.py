from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView, View

class Homeview(View):
    def get(self, *args, **kwargs):
        posts = Post.objects.all()
        context = {
            'posts': posts,
        }
        return render(self.request, 'home.html', context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

