"""wangcwblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve
import xadmin

from blog.views import BlogView, CategoryView, ArchiveView, AboutView, ContentView, TagView
from wangcwblog.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^$', BlogView.as_view(), name='home'),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^categories/$', CategoryView.as_view(), name='categories'),
    url(r'^category/(?P<category_id>[0-9]+)$', CategoryView.as_view(), name='category_id'),
    url(r'^archives/$', ArchiveView.as_view(), name='archives'),
    url(r'^tags/$', TagView.as_view(), name='tags'),
    url(r'^tag/(?P<tag_id>[0-9]+)$', TagView.as_view(), name='tag_id'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^content/(?P<article_id>[0-9]+)$', ContentView.as_view(), name='content'),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'media/(?P<path>.*)', serve, {'document_root': MEDIA_ROOT}),
]
