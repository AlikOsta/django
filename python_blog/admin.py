from django.contrib import admin
from .models import Menu, Categories, Post, Comments

admin.site.register(Menu)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'slug')
    exclude = ('slug',)


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'created_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'created_at')
    exclude = ('slug',)