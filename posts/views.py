"""post views"""
#django
from django.contrib.auth.decorators import login_required
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
    model = Post #modelo donde se toma la info
    template_name = 'posts/new.html' #template donde recibe la info
    # form_class = PostForm
    fields = ['title', 'photo']

    def form_valid(self, form): #validacion formulario
        form.instance.user = self.request.user
        form.instance.profile = self.request.user.profile
        print(form)
        form.save() #guardar datos de formtulario en bd
        return super(CreatePostView, self).form_valid(form)

    def get_success_url(self): #retorno despues de guardado exitoso
        return reverse('posts:feed')

@login_required
def like_post(request,user1,user2):
  """current user= user2 , user to follow = user1 """
  usr_id1=User.objects.get(username=user1).id
  print(usr_id1)
  usr_id2=User.objects.get(username=user2).id
  print(usr_id2)
  if (Follow.objects.filter(following=usr_id1, follower=usr_id2).count())!=0:
    print("registro ya existe..eliminando")
    Follow.objects.filter(following=usr_id1, follower=usr_id2).delete()
  else:
    print("creando registro..")
    Follow.objects.create(follower=usr_id2,following=usr_id1) 
  
  return HttpResponseRedirect(reverse('users:detail',args=[user1,]))


    

