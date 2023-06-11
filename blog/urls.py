from django.contrib.auth import views as auth_views
from django.urls import path
from blog.views import *
from blog.forms import LoginForm


app_name = "blog"

urlpatterns = [
    # path("", index, name="index"),
    path("", PostListView.as_view(), name="posts"),
    path("best/", best, name="best"),
    path("people/", PeopleListView.as_view(), name="user_list"),
    path("author/<int:pk>/", PeopleDetailView.as_view(), name="user_detail"),
    path("post/<int:pk>/", post_detail, name="post_detail"),
    path("signup/", signup, name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="blog/login.html", authentication_form=LoginForm
        ),
        name="login",
    ),
    path("new_post/", new_post, name="new_post"),
    path("post/<int:pk>/new_comment/", new_comment, name="new_comment"),
    path("rateup/<int:pk>", rate_up, name="rate_up"),
    path("ratedown/<int:pk>", rate_down, name="rate_down"),
    # path("user/<int:pk>/", people_detail, name="people_detail"),
    path("profile/<int:pk>", profile, name="profile"),
]
