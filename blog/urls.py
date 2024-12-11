
from django.contrib import admin
from django.urls import path, include
from python_blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('python_blog.urls')),
    path('',  views.main, name="main")

]
