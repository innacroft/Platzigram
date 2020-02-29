"""posts urls"""
#django
from django.urls import path
from djago.views.generic import Templateview
#views
from posts import views

urlpatterns=[
  #posts
  path(route='<str:username>/',
  view=TemplateView.as_view(template_name='users/detail'),
  name='detail'),

  path(route='users/login/',
  view='views.login_view',
  name='login'),
  
  path(route='users/logout/',
  view='views.logout',
  name='logout'),

  path(route='users/signup/',
  view='views.signup',
  name='signup'),

 path(route='users/me/profile/',
  view='views.update_profile',
  name='update_profile'),

  ]


