from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from . import models

CATEGORIES = [
    {'slug': 'python', 'name': 'Python'},
    {'slug': 'django', 'name': 'Django'},
    {'slug': 'postgresql', 'name': 'PostgreSQL'},
    {'slug': 'docker', 'name': 'Docker'},
    {'slug': 'linux', 'name': 'Linux'},
]

def main(request):
    nemu_items = models.Menu.objects.all()
    posts = models.Post.objects.filter(is_published = True)

    context = {
       "nemu_items" : nemu_items, 
       "posts" : posts,
    }

    return render(request, 'python_blog/main.html', context)


def catalog_categories(request):
    links = []
    for category in CATEGORIES:
        url=reverse('blog:category_detail', args=[category['slug']])
        links.append(f'<p><a href="{url}">{category["name"]}</a></p>')
        
    return HttpResponse(f'''
        <h1>Каталог категорий</h1>
        {''.join(links)}
        <p><a href="{reverse('blog:posts')}">К списку постов</a></p>
    ''')

def category_detail(request, category_slug):
    category = next((cat for cat in CATEGORIES
    if cat['slug'] == category_slug), None)
    if category: name = category['name']
    else: name = category_slug

    return HttpResponse(f'''
    <h1>Категория {name}</h1>
    <p><a href="{reverse('blog:categories')}">К списку категорий</a></p>
''')

def catalog_tags(request):
    return HttpResponse('Каталог тегов')

def tag_detail(request, tag_slug):
    return HttpResponse(f'Тег {tag_slug}')

def catalog_posts(request):
    return HttpResponse('Каталог постов')

def post_detail(request, post_slug):
    return HttpResponse(f'Пост {post_slug}')