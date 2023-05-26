from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Category, Post, Comment, User, Follow, Rating
from .forms import SignupForm


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


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("/login/")

    else:
        form = SignupForm()

    return render(request, "blog/signup.html", {"form": form})
