from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import F, Q
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from . import models



def main(request):
    """На главной странице отображаться сборная информация: последние посты, популярные статьи, категории.
    Выводит:
    - 6 последних опубликованных постов, отсортированных по дате обновления
    - Все доступные категории
    - 6 самых популярных постов по количеству просмотров
    Args:
        request: Объект HTTP-запроса
    Returns:
        HttpResponse: Отрендеренный шаблон main.html с контекстом
    """
    posts = models.Post.objects.select_related('category', 'author').prefetch_related('hashtags').filter(is_published=True).order_by('-updated_at')[:6]
    categories = models.Categories.objects.annotate(post_count=Count('posts'))
    popular_posts = models.Post.objects.select_related('category', 'author').prefetch_related('hashtags').filter(is_published=True).order_by('-views')[:6]

    context = {
       "posts" : posts,
       "popular_posts" : popular_posts,
       "categories" : categories,
    }

    return render(request, 'python_blog/main.html', context)


def category_detail(request, category_slug):
    """Отображает детальную страницу категории.
    Выводит все опубликованные посты, относящиеся к выбранной категории.
    Args:
        request: Объект HTTP-запроса
        category_slug: Слаг категории для фильтрации
    Returns:
        HttpResponse: Отрендеренный шаблон category_detail.html с контекстом
    """
    category = models.Categories.objects.get(slug=category_slug)
    posts = models.Post.objects.select_related('category', 'author').prefetch_related('hashtags').filter(category=category, is_published=True)

    context = {
       "category" : category,
        "posts" : posts,
        
    }

    return render(request, 'python_blog/category_detail.html', context)


def catalog_categories(request):
    """Отображает каталог всех категорий блога. Не понимаю зачем этот шаблон, но он есть в макете.
    Выводит список всех доступных категорий.
    Args:
        request: Объект HTTP-запроса
    Returns:
        HttpResponse: Отрендеренный шаблон categories.html с контекстом
    """
    categories = models.Categories.objects.annotate(post_count=Count('posts'))

    context = {
       "categories" : categories,
    }

    return render(request, 'python_blog/categories.html', context)


def about(request):
    """Отображает страницу "О нас".
    Args:
        request: Объект HTTP-запроса
    Returns:
        HttpResponse: Отрендеренный шаблон about.html
    """

    return render(request, 'python_blog/about.html')


def post_detail(request, post_slug):
    """Отображает детальную страницу поста.    
    Выводит содержимое поста и все опубликованные комментарии к нему.
    Args:
        request: Объект HTTP-запроса
        post_slug: Слаг поста для поиска
    Returns:
        HttpResponse: Отрендеренный шаблон post_detail.html с контекстом
    """
    post = models.Post.objects.select_related('category', 'author').prefetch_related('hashtags').get(slug=post_slug)
    viewed_posts = request.session.get('viewed_posts', [])

    if post.id not in viewed_posts:
        models.Post.objects.filter(pk=post.pk).update(views=F('views') + 1)
        viewed_posts.append(post.id)
        request.session['viewed_posts'] = viewed_posts
    
    comments = models.Comments.objects.filter(post=post, is_published=True)

    context = {
        "post": post,
        "comments": comments,
    }
    return render(request, 'python_blog/post_detail.html', context)


def catalog_posts(request):
    """Отображает каталог всех постов с фильтрацией по дате обновления и пагинацией по 10 постов на странице.
    Выводит:
    - Список всех категорий
    - Все опубликованные посты, отсортированные по дате обновления
    Args:
        request: Объект HTTP-запроса
    Returns:
        HttpResponse: Отрендеренный шаблон catalog_posts.html с контекстом
    """

    categories = models.Categories.objects.annotate(post_count=Count('posts'))
    posts = models.Post.objects.select_related('category', 'author').prefetch_related('hashtags').filter(is_published=True)
    
    search_query = request.GET.get('search_query', '')
    
    if search_query:
        q_object = Q()
        
        # Check which search fields are selected
        if request.GET.get('search_content') == '1':
            q_object |= Q(content__icontains=search_query)
        if request.GET.get('search_title') == '1':
            q_object |= Q(title__icontains=search_query)
        if request.GET.get('search_tags') == '1':
            q_object |= Q(hashtags__name__icontains=search_query)
            
        # If no checkboxes selected, search in content by default
        if not q_object:
            q_object = Q(content__icontains=search_query)
            
        posts = posts.filter(q_object).distinct()
        
        # Add search results message
        messages.info(request, f'Найдено {posts.count()} результатов по запросу "{search_query}"')

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page', 1)
    posts = paginator.get_page(page_number)

    context = {
        "categories": categories,
        "posts": posts,
    }
    
    return render(request, 'python_blog/catalog_posts.html', context)


def catalog_tags(request):
    return HttpResponse('Каталог тегов')

def tag_detail(request, tag_slug):
    return HttpResponse(f'Тег {tag_slug}')


def about(request):
    return render(request, 'python_blog/about.html')

