from django.views.generic.list import ListView
from django.views.generic.detail import DetailView #библиотека для работы со списками (вывода списка записей)
from django.urls import include, path
from news.models import Articles
from . import views


"""Для того, чтобы, находясь в директории /news, отображались списком все статьи из БД, используем ListView.as_view,
после указываем запрос к БД, а именно к таблице Article (queryset=Articles), о выводе всех объектов (.objects.all())
и сортировке по новой дате, отображая не более 20 рез-тов (.order_by("-date")[:20]).
Для использования шаблона на страницах приложения используем template_name='news/posts.html' с файлом щаблона, вместо view.py
"""
urlpatterns = [
    #path('', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20], template_name='news/posts.html')),
    #path('<int:pk>/', DetailView.as_view(model=Articles, template_name="news/post.html")),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]
