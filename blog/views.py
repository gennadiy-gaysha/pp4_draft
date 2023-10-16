from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Country
from .forms import PostForm

from .filters import PostFilter


class PostList(ListView):
    model = Post
    template_name = 'blog/home.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = Post.objects.filter(status=1).order_by('-created_on')
        filter_data = PostFilter(self.request.GET, queryset=queryset)
        return filter_data.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostDetails(DetailView):
    model = Post
    template_name = 'blog/post_details.html'


# LoginRequiredMixin provides functionality to other CreatePost class
# without being the parent class of this class
class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'

    # fields = ('title', 'featured_image', 'content')

    def form_valid(self, form):
        """
        - form_valid automatically sets the author to the logged-in user.
        - the form argument in the form_valid method of a Django class-based
        CreateView is automatically passed to the method by Django's view
        processing mechanism. It represents the form instance that is being
        processed, and it comes from the form submission.
        - form_valid() is a method that is being overriden in CreatePost view
        to provide custom logic that should be executed when the submitted
        form data is valid
        - the currently logged-in user: self.request.user is assigned
        to the author form.instance.author
        - super() is used to call the parent class's method. It calls the
        form_valid method of the parent class (CreateView) to ensure that
        the standard behavior of the CreateView is executed.
        """
        form.instance.author = self.request.user
        messages.success(self.request, 'Post created successfully.')
        return super().form_valid(form)


class UpdatePost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/update_post.html'

    def form_valid(self, form):
        """
        Sets post status to DRAFT after updating the post
        """
        # Get the post being updated
        post = form.instance
        # Set the status to 0 (Draft)
        post.status = 0
        # Save the updated post with the new status
        post.save()
        # Add a success message
        messages.success(self.request, 'Post updated successfully.')

        return redirect('post-details', slug=post.slug)


class DeletePost(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Post deleted successfully.')  # Add this line to display a success message
        return super().delete(request, *args, **kwargs)


class ShowCountry(DetailView):
    model = Country
    template_name = 'blog/show_country.html'


def search_country(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        return render(request, 'blog/show_search_country.html', {'searched': searched})
    else:
        return render(request, 'blog/show_search_country.html', {})

