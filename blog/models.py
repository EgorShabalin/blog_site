from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    url = models.SlugField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


'''class Users(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    avatar = models.ImageField(default=None, upload_to="avatars")
    status = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"'''


class Posts(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(default=None, upload_to="post_imgs")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    posted = models.BooleanField(default=False)
    url = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"


class Comments(models.Model):
    author = models.ForeignKey(
        User, related_name="comment_author", on_delete=models.SET_NULL, null=True
    )
    text = models.TextField()
    img = models.ImageField(default=None, upload_to="comment_imgs")
    parent = models.ForeignKey(
        User, related_name="user_commented", on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    posted = models.BooleanField(default=False)
    url = models.SlugField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.text[0:20]

    class Meta:
        verbose_name_plural = "Comments"


class Follows(models.Model):
    following_user = models.ForeignKey(
        User, related_name="follower", on_delete=models.CASCADE
    )
    follows_user = models.ForeignKey(
        User, related_name="follows", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Rating(models.Model):
    user = models.ForeignKey(
        User, related_name="follower", on_delete=models.SET_NULL, null=True
    )
    likes = models.CharField(max_length=1, default="0")
    dislikes = models.CharField(max_length=1, default="0")
    post = models.ForeignKey(Posts, on_delete=models.SET_NULL, null=True)
    comment = models.ForeignKey(Comments, on_delete=models.SET_NULL, null=True)
