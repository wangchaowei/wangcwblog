# coding:utf-8
# __author__ = 'wangchaowei'
# __date__ = '17/5/16 19:38'


import xadmin
from xadmin import views
from .models import AuthorProfile, Article, Comment, Category, Tag


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = '王朝伟-——博客后台管理系统'
    site_footer = 'wangchaowei'
    menu_style = 'accordion'


class ArticleAdmin(object):
    list_display = ['author', 'title', 'digest', 'comment', 'add_time']
    search_fields = ['author', 'title', 'digest', 'comment']
    list_filter = ['author', 'title', 'digest', 'comment', 'add_time']
    style_fields = {'text': 'ueditor', 'digest': 'ueditor'}



class CommentAdmin(object):
    list_display = ['text', 'nick_name', 'email', 'add_time']
    search_fields = ['text', 'nick_name', 'email']
    list_filter = ['text', 'nick_name', 'email', 'add_time']
    style_fields = {'text': 'ueditor'}

class AuthorProfileAdmin(object):
    list_display = ['name', 'gender', 'email', 'nick_name']
    search_fields = ['name', 'gender', 'email', 'nick_name']
    list_filter = ['name', 'gender', 'email', 'nick_name']


class CategoryAdmin(object):
    list_display = ['name', 'article']
    search_fields = ['name', 'article']
    list_filter = ['name', 'article']


class TagAdmin(object):
    list_display = ['name', 'article']
    search_fields = ['name', 'article']
    list_filter = ['name', 'article']

xadmin.site.register(AuthorProfile, AuthorProfileAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Comment, CommentAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
