# Generated by Django 5.1.4 on 2025-01-11 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_blog', '0002_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='python_blog.categories', verbose_name='Категория'),
        ),
    ]
