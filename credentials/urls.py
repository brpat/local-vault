from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("base", views.base, name="base"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("postsignup", views.postsignup, name="postsignup"),
    path('myvault', views.myvault, name='myvault')
]

