
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

urlpatterns = [
    path('<str:name>/', views.index, name='index')
]
