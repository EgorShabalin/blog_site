from django.contrib.auth import views as auth_views
from django.urls import path
from blog.views import index, post_detail, people, signup
from blog.forms import LoginForm


app_name = "blog"

urlpatterns = [
    path("", index, name="index"),
    path("best", index, name="best"),
    path("people", people, name="people"),
    path("<int:pk>/", post_detail, name="post_detail"),
    path("signup/", signup, name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="blog/login.html", authentication_form=LoginForm
        ),
        name="login",
    ),
]
