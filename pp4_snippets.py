from django_summernote.widgets import SummernoteWidget


class PostDetails(generic.DetailView):
    template_name = 'blog/post_details.html'
    queryset = Post.objects.filter(status=2)
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comments.filter(approved=True).order_by("-created_on")
        context['liked'] = post.likes.filter(id=self.request.user.id).exists()
        return context
# ======================================

