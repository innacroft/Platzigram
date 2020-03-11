
# Django
from django.http import HttpResponseRedirect,HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView

# Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile,Follow

# Forms
from users.forms import SignupForm
# Create your views here.


class UserDetailView(LoginRequiredMixin, DetailView):  #loginreq, sea requerido login
  """User detail view"""
  template_name='users/detail.html'
  slug_field='username'
  slug_url_kwarg='username' #keyword argument...
  queryset= User.objects.all()
  context_object_name='user'
 
  def get_context_data(self,**kwargs):
    """add users posts to context"""
    context=super().get_context_data(**kwargs)
    user=self.get_object() #este hace el query para user
    context['posts']=Post.objects.filter(user=user).order_by('-created')
    #conteo de publicaciones
    usr=Profile.objects.get(user=user) 
    usr.posts_count=Post.objects.filter(user=user).count()
    usr.save()
    

  #  usr1=User.objects.get(username=usr)
    usr_id=(User.objects.get(username=usr)).id
    #conteo seguidores
    context['followers']=Follow.objects.filter(following=usr_id).count()
    #conteo de siguiendo
    context['following']=Follow.objects.filter(follower=usr_id).count()
    #siguiendo o no:
     
    return context
    

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})

class LoginView(auth_views.LoginView):
  """loginview!"""
  template_name= 'users/login.html'

class SignupView(FormView):
    """Users sign up view."""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)

@login_required
def logout_view(request):
  """logout a user"""
  return redirect('users:login')
  

def follow_user(request,user1,user2):
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

#    context['is_following']=Follow.objects.filter(following=usr_id, follower=usr_id2).count()



