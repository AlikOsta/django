from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from . import models

def main(request):
    posts = models.Post.objects.filter(is_published = True).order_by('-updated_at')[:5]
    categoris = models.Categories.objects.all()
    popular_posts = models.Post.objects.filter(is_published=True).order_by('-views')[:5]

    context = {
       "posts" : posts,
       "popular_posts" : popular_posts,
       "categories" : categoris,
       "active_page" : "main",
    }

    return render(request, 'python_blog/main.html', context)


def category_detail(request, category_slug):
    category = models.Categories.objects.get(slug=category_slug)
    posts = models.Post.objects.filter(category=category, is_published=True)

    context = {
       "category" : category,
        "posts" : posts,
    }

    return render(request, 'python_blog/category_detail.html', context)


def catalog_categories(request):
    categories = models.Categories.objects.all()

    context = {
       "categories" : categories,
       "active_page" : "blog:categories",
    }

    return render(request, 'python_blog/categories.html', context)


def about(request):
    return render(request, 'python_blog/about.html')



def catalog_tags(request):
    return HttpResponse('Каталог тегов')

def tag_detail(request, tag_slug):
    return HttpResponse(f'Тег {tag_slug}')

def catalog_posts(request):
    return HttpResponse('Каталог постов')

def post_detail(request, post_slug):
    post = models.Post.objects.get(slug=post_slug)
    comments = models.Comments.objects.filter(post=post, is_published=True)

    context = {
        "post": post,
        "comments": comments,
    }
    
    return render(request, 'python_blog/post_detail.html', context)