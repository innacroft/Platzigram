
# Django
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
from users.models import Profile

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
  
