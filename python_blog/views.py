from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from . import models

def main(request):
    nemu_items = models.Menu.objects.all()
    posts = models.Post.objects.filter(is_published = True).order_by('-updated_at')[:5]
    categoris = models.Categories.objects.all()
    popular_posts = models.Post.objects.filter(is_published=True).order_by('-views')[:5]

    context = {
       "nemu_items" : nemu_items, 
       "posts" : posts,
       "popular_posts" : popular_posts,
       "categories" : categoris,
    }

    return render(request, 'python_blog/main.html', context)


def category_detail(request, category_slug):
    nemu_items = models.Menu.objects.all()
    category = models.Categories.objects.get(slug=category_slug)
    posts = models.Post.objects.filter(category=category, is_published=True)


    context = {
       "nemu_items" : nemu_items, 
       "categories" : category,
        "posts" : posts,
    }

    return render(request, 'python_blog/category_detail.html', context)



def catalog_categories(request):
    categoris = models.Categories.objects.all()
    nemu_items = models.Menu.objects.all()

    context = {
       "nemu_items" : nemu_items, 
       "categories" : categoris,
    }

    return render(request, 'python_blog/categories.html', context)



def catalog_tags(request):
    return HttpResponse('Каталог тегов')

def tag_detail(request, tag_slug):
    return HttpResponse(f'Тег {tag_slug}')

def catalog_posts(request):
    return HttpResponse('Каталог постов')

def post_detail(request, post_slug):
    return HttpResponse(f'Пост {post_slug}')