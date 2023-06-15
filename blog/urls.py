from django.contrib.auth import views as auth_views
from django.urls import path
from blog.views import *
from blog.forms import LoginForm


app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="posts"),
    path("best/", best, name="best"),
    path("people/", PeopleListView.as_view(), name="user_list"),
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
    path("profile/<int:pk>", profile, name="profile"),
    path("following/", authors_you_follow, name="authors_you_follow"),
    path("profile_posts/<int:pk>", profile_posts, name="profile_posts"),
    path("profile_follows/<int:pk>/", profile_follows, name="profile_follows"),
    path(
        "profile_followed_by/<int:pk>/", profile_followed_by, name="profile_followed_by"
    ),
]
