# coding:utf-8
from django.contrib import admin
from blog.models import *


# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,
         {'fields': ('title', 'desc', 'content', 'tag', 'category', 'user')}
         ),
        ('高级设置',
         {
             'classes': ('collapse',),
             'fields': ('is_recommend', 'click_count')
         }
         )
    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'article']
    raw_id_fields = ['article']

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     article1 = None
    #     if db_field.name == 'article':
    #         article1 = db_field.formfield['article']
    #     if db_field.name == 'pid':
    #         print article1
    #         kwargs["queryset"] = Comment.objects.filter(article=article1)
    #     return super(CommentAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Comment, CommentAdmin)


class ResponseAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'article', 'pid', 'rid']
    raw_id_fields = ['article', 'pid', 'rid']


admin.site.register(Response, ResponseAdmin)
admin.site.register(Links)
admin.site.register(Ad)
