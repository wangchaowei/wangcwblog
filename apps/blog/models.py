# coding:utf-8
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from collections import defaultdict
from DjangoUeditor.models import UEditorField


class Comment(models.Model):
    text = UEditorField(verbose_name=u'评论内容',width=600, height=300, imagePath="blog/ueditor/",
                        filePath="blog/ueditor/", default='')  # imagePath相对于media_root
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    def __unicode__(self):
        return self.nick_name

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = verbose_name


class AuthorProfile(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'姓名', default=u'王朝伟')
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称')
    gender = models.CharField(max_length=7, choices=(('male', u'男'), ('female', u'女')), default='male',
                              verbose_name=u'性别')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    # mobile = models.CharField(max_length=11, blank=True, null=True)
    # image = models.ImageField(upload_to='image/%Y/%m', default=u'image/default.png', max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'作者信息'
        verbose_name_plural = verbose_name


class ArticleManager(models.Manager):
    """
    继承自默认的 Manager ，为其添加一个自定义的 archive 方法
    """
    def archive(self):
        date_list = Article.objects.datetimes('created_time', 'month', order='DESC')
        # 获取到降序排列的精确到月份且已去重的文章发表时间列表
        # 并把列表转为一个字典，字典的键为年份，值为该年份下对应的月份列表
        date_dict = defaultdict(list)
        for d in date_list:
            date_dict[d.year].append(d.month)
        # 模板不支持defaultdict，因此我们把它转换成一个二级列表，由于字典转换后无序，因此重新降序排序
        return sorted(date_dict.items(), reverse=True)


class Article(models.Model):
    objects = ArticleManager()
    author = models.ForeignKey(AuthorProfile, verbose_name=u'作者')
    title = models.CharField(max_length=200, verbose_name=u'标题')
    digest = UEditorField(width=600, height=300, imagePath="blog/ueditor/",
                        filePath="blog/ueditor/", default='', verbose_name=u'摘要')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    comment = models.ForeignKey(Comment, verbose_name=u'评论', null=True, blank=True)
    text = UEditorField(verbose_name=u'文章内容', width=600, height=300, imagePath="blog/ueditor/",
                        filePath="blog/ueditor/", default='')  # imagePath相对于media_root


    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'博文'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'标签名')
    article = models.ManyToManyField(Article, blank=True, verbose_name=u'文章')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = verbose_name


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'类名')
    article = models.ManyToManyField(Article, blank=True, verbose_name=u'文章')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'分类'
        verbose_name_plural = verbose_name


