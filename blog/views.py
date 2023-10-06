from django.views.generic import ListView, DetailView

from .models import Post

class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/home.html'
    paginate_by = 3

class PostDetails(DetailView):
    model = Post
    template_name = 'blog/post_details.html'

