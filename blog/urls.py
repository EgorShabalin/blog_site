from django.urls import path
from blog.views import index

urlpatterns = [
    path("", index, name="index"),
    path("best", index, name="best"),
    path("people", index, name="people"),
]
