from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Post

context = {
    'posts' : Post.objects.order_by('publish_date'),
}


def home(request):
    return render(request, 'index.html', context=context)

def post(request, post_url):
    post_context = {
        'posts' : Post.objects.filter(url=post_url),
    }
    print(post_context)
    return render(request, 'post.html', context=post_context)