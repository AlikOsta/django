from django.shortcuts import render
from django.http import HttpResponse
from . import models



def catalog_categories(request):
    return HttpResponse('Каталог категорий')

def category_detali(request, category_slug):
    return HttpResponse(f'Категория {category_slug}')

def catalog_tags(request):
    return HttpResponse('Каталог тегов')

def tag_detail(request, tag_slug):
    return HttpResponse(f'Тег {tag_slug}')

def catalpg_posts(request):
    return HttpResponse('Каталог постов')

def posts_detail(request, post_slug):
    return HttpResponse(f'Пост {post_slug}')