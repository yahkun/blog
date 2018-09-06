# -*- coding:utf-8 -*-

from django.contrib import admin

from models import *

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'desc', 'category', 'click_count', 'date_publish')
    list_display_links = ('title', 'desc', )
    list_editable = ('click_count', 'category', 'date_publish', )

    fieldsets = (
        ('基础设置', {
            'fields': ('title', 'en_title', 'desc', 'content', 'user', 'category', 'tag')
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('click_count', 'is_recommend', 'date_publish')
        }),
    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )


class CommentAdmin(admin.ModelAdmin):

    list_display = ('username', 'content', 'pid', 'article', 'email', 'date_publish')
    list_display_links = ('content',)
    list_editable = ()

    # fieldsets = (
    #     ('基础设置', {
    #         'fields': ('title', 'en_title', 'desc', 'content', 'user', 'category', 'tag')
    #     }),
    #     ('高级设置', {
    #         'classes': ('collapse',),
    #         'fields': ('click_count', 'is_recommend', 'date_publish')
    #     }),
    # )


class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'first_name', 'last_name', 'email', 'qq', 'mobile', 'url', 'date_joined')
    list_display_links = ('username',)
    list_editable = ()
    

admin.site.register(User, UserAdmin)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Links)
admin.site.register(Ad)
