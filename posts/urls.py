"""Posts URLs."""

# Django
from django.urls import path

# Views
from posts import views

urlpatterns = [

    path(
        route='',
        view=views.PostsFeedView.as_view(),
        name='feed'
    ),

    path(
        route='posts/<int:pk>',
        view=views.PostDetailView.as_view(),
        name='post_detail'
    ),

    path(
        route='posts/new/',
        view=views.CreatePostView.as_view(),
        name='create'
    ),

 #   path(
 #       route='<str:user1>/<str:user2>/',
 #       view=views.like_post,
  #      name='like_post'
 #   ),
  
]