
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
# url posts/..

urlpatterns = [
    #category
    path('categories/', views.catalog_categories),
    path('categories/<slug:category_slug>/', views.category_detali, ),
    # tag
    path('tags/', views.catalog_tags),
    path('tags/<slug:tag_slug>/', views.tag_detail),
    #posts
    path('', views.catalpg_posts),
    path('<slug:post_slug>/', views.posts_detail),
]