from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Category, Post, Comment, User, Follow, Rating
from .forms import SignupForm, NewPostForm, NewCommentForm


# Create your views here.
def index(request):
    posts = Post.objects.filter(posted=True)[0:10]
    post_category = Category.objects.all()
    comments = Comment.objects.all()
    for post in posts:
        comments = Comment.objects.filter(parent=post, posted=True)
        comments_count = comments.count()

    return render(
        request,
        "blog/index.html",
        {
            "posts": posts,
            "post_category": post_category,
            "comments_count": comments_count,
        },
    )


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(parent=post, posted=True)
    comments_count = comments.count()
    rating = Rating.objects.filter(post=post)

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comments_count": comments_count,
            "rating": rating,
        },
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


@login_required
def new_post(request):
    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect("/new_post/", pk=post.id)

    else:
        form = NewPostForm()

    return render(request, "blog/new_post_form.html", {"form": form})


@login_required
def new_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = NewCommentForm(request.POST, request.FILES)

        if form.is_valid() and post.id == pk:
            comment = form.save(commit=False)
            comment.parent = post
            comment.author = request.user
            comment.save()

            return redirect("blog:post_detail", pk=pk)

    else:
        form = NewCommentForm()

    return render(request, "blog/new_comment_form.html", {"form": form, "post": post})


class PeopleListView(generic.ListView):
    model = User
