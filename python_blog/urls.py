
from django.urls import path
from . import views

'''
типы конверторов: 
str - строки, любые символы кроме слэша '/' (по умолчанию)
int - положительные целые числа включая 0
slug - ASCII буквы/цифры, дефисы и подчеркивания
uuid - уникальные идентификаторы UUID
path - строки, включая слэши '/'

Пример:
path('<str:name>/', views.index, name='index')
'''

app_name = 'blog'

urlpatterns = [
    # about
    path('about/', views.about, name="about"),
    # category
    path('categories/', views.catalog_categories, name='categories'),
    path('categories/<slug:category_slug>/', views.category_detail, name="category_detail"),
    # tag 
    path('tags/', views.catalog_tags, name="tags"),
    path('tags/<slug:tag_slug>/', views.tag_detail, name="tag_detail"),
    # posts
    path('', views.catalog_posts, name="posts"),
    path('<slug:post_slug>/', views.post_detail, name="post_detail"),
    


]