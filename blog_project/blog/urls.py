# coding:utf-8
from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^base/$', views.base),
    url(r'^$', views.index, name='index'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^tag/$', views.tag, name='tag'),
    url(r'^category/$', views.category, name='category'),
    url(r'^article/$', views.article, name='article'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.do_login, name='login'),
    url(r'^logout/$', views.do_logout, name='logout'),
    url(r'^comment/$', views.comment_post, name='comment'),
    url(r'^comment_delete/$', views.comment_delete, name='comment_delete'),
]