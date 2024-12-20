from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from . import models

def main(request):
    nemu_items = models.Menu.objects.all()
    posts = models.Post.objects.filter(is_published = True)

    context = {
       "nemu_items" : nemu_items, 
       "posts" : posts,
    }

    return render(request, 'python_blog/main.html', context)


def catalog_categories(request):
    categories = models.Categories.objects.all()

    context= {
        "categories" : categories
    }

    return render(request, 'python_blog/categories.html', context)    

def category_detail(request, category_slug):
    pass

def catalog_tags(request):
    return HttpResponse('Каталог тегов')

def tag_detail(request, tag_slug):
    return HttpResponse(f'Тег {tag_slug}')

def catalog_posts(request):
    return HttpResponse('Каталог постов')

def post_detail(request, post_slug):
    return HttpResponse(f'Пост {post_slug}')