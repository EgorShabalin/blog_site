from django.shortcuts import render, get_object_or_404
from blog.models import Category, Post, Comment, User, Follow, Rating


# Create your views here.
def index(request):
    posts = Post.objects.filter(posted=True)[0:10]
    categories = Category.objects.all()
    comments = Comment.objects.all()
    return render(
        request,
        "blog/index.html",
        {"posts": posts, "categories": categories, "comments": comments},
    )


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.all()
    return render(
        request, "blog/post_detail.html", {"post": post, "comments": comments}
    )


def people(request):
    authors = User.objects.all()
    folowers = Follow.objects.all()
    return render(
        request, "blog/people.html", {"authors": authors, "followers": folowers}
    )


def rating(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    current_rating = post.rating
