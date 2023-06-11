from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Category, Post, Comment, User, Profile
from .forms import SignupForm, NewPostForm, NewCommentForm


# Create your views here.
class PostListView(generic.ListView):
    model = Post
    paginate_by = 10


class PeopleListView(generic.ListView):
    model = User
    paginate_by = 10


class PeopleDetailView(generic.DetailView):
    model = User


def people_detail(request, pk):
    users = User.objects.all()
    posts = Post.objects.all()

    return render(request, "blog/user_detail.html", {"posts": posts, "users": users})


def best(request):
    posts = Post.objects.all()
    posts = Post.objects.filter(posted=True).order_by("-likes")[0:10]

    return render(request, "blog/post_list.html", {"post_list": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(parent=post, posted=True)
    comments_count = comments.count()
    rating = post.likes_count()

    if request.method == "POST":
        current_user_profile = request.user.profile
        user_to_follow = post.author
        current_user_profile.follows.add(user_to_follow.profile)
        action = request.POST["follow"]
        if action == "unfollow":
            current_user_profile.follows.remove(user_to_follow.profile)

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


@login_required
def rate_up(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    if post.likes.filter(id=request.user.id).exists():
        pass
    elif post.dislikes.filter(id=request.user.id).exists():
        post.dislikes.remove(request.user.id)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse("blog:post_detail", args=[str(pk)]))


@login_required
def rate_down(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.dislikes.add(request.user)

    return HttpResponseRedirect(reverse("blog:post_detail", args=[str(pk)]))


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


@login_required
def profile(request, pk):
    profile = Profile.objects.get(current_user_id=pk)
    post_count = Post.objects.filter(author=profile.current_user).count()
    comment_count = Comment.objects.filter(author=profile.current_user).count()

    if request.method == "POST":
        current_user_profile = request.user.profile
        user_to_follow = profile.current_user
        current_user_profile.follows.add(user_to_follow.profile)
        action = request.POST["follow"]
        if action == "unfollow":
            current_user_profile.follows.remove(user_to_follow.profile)

    return render(
        request,
        "blog/profile.html",
        {"profile": profile, "post_count": post_count, "comment_count": comment_count},
    )
