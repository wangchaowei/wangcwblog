# coding:utf-8
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView
# import markdown2
# from urllib import urlencode

from .models import Article, AuthorProfile, Comment, Category, Tag
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


class BlogView(View):

    def get(self, request):
        articles = Article.objects.all().order_by('-add_time')
        # 对博文进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(articles, 4, request=request)  # 5是每一页显示的数量
        articles = p.page(page)

        return render(request, 'blog/home.html', {
            'active': 'home',
            'articles': articles,
            'tags_num': Tag.objects.count(),
            'category_num': Category.objects.count(),
            'article_num': Article.objects.count(),
        })


class ArchiveView(View):
    def get(self, request):
        dates = Article.objects.datetimes('add_time', 'second', order='DESC')
        articles = Article.objects.all().order_by('-add_time').iterator()
        articles_id = Article.objects.all().order_by('-add_time').iterator()
        articles_num = Article.objects.count()
        return render(request, 'blog/archive.html', {
            'articles': articles,
            'articles_id': articles_id,
            'dates': dates,
            'active': 'archives',
            'tags_num': Tag.objects.count(),
            'category_num': Category.objects.count(),
            'article_num': articles_num,
            'archive_article_num': articles_num,
            'title': u'时间归档',
        })


class ContentView(View):
    def get(self, request, article_id):
        article = Article.objects.filter(id=article_id)
        return render(request, 'blog/content.html', {
            'article': article[0],
            'tags_num': Tag.objects.count(),
            'category_num': Category.objects.count(),
            'article_num': Article.objects.count(),
        })


class CategoryView(View):

    def get(self, request, category_id=None):
        if category_id is not None:
            category = Category.objects.filter(id=category_id)
            articles = category[0].article.get_queryset().order_by('-add_time')

            # 对博文进行分页
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1

            p = Paginator(articles, 4, request=request)  # 5是每一页显示的数量
            articles = p.page(page)

            return render(request, 'blog/home.html', {
                'articles': articles,
                'active': 'categories',
                'tags_num': Tag.objects.count(),
                'category_num': Category.objects.count(),
                'article_num': Article.objects.count(),
            })

        categories = Category.objects.all()
        return render(request, 'blog/category.html', {
            'categories': categories,
            'active': 'categories',
            'tags_num': Tag.objects.count(),
            'category_num': categories.count(),
            'article_num': Article.objects.count(),
        })


class TagView(View):

    def get(self, request, tag_id=None):
        if tag_id is not None:
            tag = Tag.objects.filter(id=tag_id)
            tag_name = tag.values('name')[0]['name']

            articles = tag[0].article.all()
            articles_id = tag[0].article.all()
            articles_num = articles.count()

            dates = articles.datetimes('add_time', 'second', order='DESC')
            articles = articles.order_by('-add_time').iterator()
            articles_id = articles_id.order_by('-add_time').iterator()
            return render(request, 'blog/archive.html', {
                'articles': articles,
                'articles_id': articles_id,
                'active': 'tags',
                'dates': dates,
                'tags_num': Tag.objects.count(),
                'archive_article_num': articles_num,
                'category_num': Category.objects.count(),
                'article_num': Article.objects.count(),
                'title': '%s 标签' % tag_name,
            })

        tags = Tag.objects.all()
        return render(request, 'blog/tags.html', {
            'tags': tags,
            'active': 'tags',
            'tags_num': tags.count(),
            'category_num': Category.objects.count(),
            'article_num': Article.objects.count(),
        })


class AboutView(View):
    def get(self, request):
        return render(request, 'blog/about.html', {
            'active': 'about',
            'tags_num': Tag.objects.count(),
            'category_num': Category.objects.count(),
            'article_num': Article.objects.count(),
        })

