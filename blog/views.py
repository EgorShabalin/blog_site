from django.shortcuts import render
from blog.models import Category, Post


# Create your views here.
def index(request):
    posts = Post.objects.filter(posted=True)[0:10]
    categories = Category.objects.all()
    return render(
        request, "blog/index.html", {"posts": posts, "categories": categories}
    )
