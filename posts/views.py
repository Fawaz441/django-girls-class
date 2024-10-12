from django.shortcuts import render
from posts.models import Post


def homepage(request):
    posts = Post.objects.all()
    context = {"gender": "Male", "posts": posts}
    return render(request, 'posts/list.html', context)
