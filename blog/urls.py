from django.urls import path
from blog.views import index, post_detail, people


app_name = "blog"

urlpatterns = [
    path("", index, name="index"),
    path("best", index, name="best"),
    path("people", people, name="people"),
    path("<int:pk>/", post_detail, name="post_detail"),
]
