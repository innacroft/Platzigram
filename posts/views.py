"""post views"""
#django

from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
#forms
from posts.forms import PostForm
#models
from posts.models import Post
# #utlilities

# Create your views here.

class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name='posts'

class PostsFeedView(LoginRequiredMixin,ListView):
    """Return all published posts"""
    template_name= 'posts/feed.html'
    model=Post
    ordering=('-created')
    paginate_by = 30 
    context_object_name='posts'

class CreatePostView(LoginRequiredMixin,CreateView):
    """Create a new post"""
    model = Post
    template_name = 'posts/new.html'
    # form_class = PostForm
    fields = ['title', 'photo']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.profile = self.request.user.profile
        print(form)
        form.save()
        return super(CreatePostView, self).form_valid(form)

    def get_success_url(self):
        return reverse('posts:feed')




    

