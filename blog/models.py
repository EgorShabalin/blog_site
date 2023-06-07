from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # url = models.SlugField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(default=None, upload_to="post_imgs", blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, blank=False, null=False
    )
    likes = models.ManyToManyField(User, related_name="post_likes")
    dislikes = models.ManyToManyField(User, related_name="post_dislikes")
    comments = models.IntegerField(default=0, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    posted = models.BooleanField(default=False)
    # url = models.SlugField(max_length=200, unique=True)

    def likes_count(self):
        return self.likes.count()

    def dislikes_count(self):
        return self.dislikes.count()

    def rating(self):
        rating = int(self.likes.count() - self.dislikes.count())
        return rating

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "Posts"


class Comment(models.Model):
    author = models.ForeignKey(
        User, related_name="comment_author", on_delete=models.DO_NOTHING, null=True
    )
    text = models.TextField()
    img = models.ImageField(
        default=None, upload_to="comment_imgs", blank=True, null=True
    )
    parent = models.ForeignKey(
        Post, related_name="post_commented", on_delete=models.DO_NOTHING, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    posted = models.BooleanField(default=False)
    # url = models.SlugField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.text[0:20]

    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "Comments"


class Follow(models.Model):
    follows_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
