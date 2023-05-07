from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign-up', views.signUp, name='sign_up'),
    path('sign-in', views.signIn, name='sign_in'),
    path('log-out', views.logOut, name='log_out'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('like-post', views.like_post, name='like-post'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),

]