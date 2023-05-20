from django.shortcuts import render
from .models import *

# Create your views here.
def blog_list(request):
    blog_posts = BlogPost.objects.all().order_by("-created_at")
    context = {"blog_posts": blog_posts}
    return render(request, "blog/blog_list.html", context)
