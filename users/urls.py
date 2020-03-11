"""Users URLs."""

# Django
from django.urls import path

# View
from users import views


urlpatterns = [

    # Management
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='logout/',
        view=views.logout_view,
        name='logout'
    ),
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route='me/profile/',
        view=views.UpdateProfileView.as_view(),
        name='update_profile'
    ),

    # Posts
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

    path(
        route='<str:user1>/<str:user2>/',
        view=views.follow_user,
        name='follow'
    ),



]