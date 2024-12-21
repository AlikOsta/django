from django.db import models
from django.contrib.auth.models import User
from slugify import slugify


class Menu(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.CharField(max_length=100, verbose_name="URL")

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class Categories(models.Model):
    '''Модель для категорий'''
    category_name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.category_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tags(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    '''Модель для постов'''
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Автор')
    title = models.CharField(max_length=200, unique=True, verbose_name='Заголовок')
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(max_length=500, verbose_name='Содержание')
    hashtags = models.ManyToManyField(Tags, blank=True)
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    likes = models.IntegerField(default=0, verbose_name='Лайки')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    image = models.ImageField(upload_to='media/posts/')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comments(models.Model):
    '''Модель для комментариев'''
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    content = models.TextField(max_length=500, verbose_name='Комментарий')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return f"Комментарий от {self.author} на пост '{self.post}'"

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
