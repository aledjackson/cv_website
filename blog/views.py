from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog.models import BlogPost


def blogHome(request) -> HttpResponse:
    titles = BlogPost.fetchTitles()
    return render(request, 'blog/list.html', {'titles' : titles})

def blogPost(request, title) -> HttpResponse:
    query = BlogPost.fetchPost(title)
    if len(query) >= 1:
        post = query[0]
        return render(request, 'blog/post.html', {'title': post.title, 'blog_text': post.content})
    else:
        return render(request, 'blog/post.html')