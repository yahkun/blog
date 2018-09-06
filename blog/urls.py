from django.conf.urls import url
from blog.views import *

urlpatterns = [
    
    url(r'^$', home, name='index'),
    
    url(r'^archive/$', archive, name='archive'),
    
    url(r'^article/(?P<id>\d+).html$', article, name='article'),
    
    url(r'^articles/$', article, name='articles'),
    
    url(r'^comment/post/$', comment_post, name='comment_post'),
    
    url(r'^signout$', signout, name='logout'),
    
    url(r'^signup', signup, name='reg'),
    
    url(r'^signin', signin, name='login'),
    
    url(r'^categorys/about$', about, name='about'),
    url(r'^categorys/(?P<category>\w+)$', category, name='category'),
    
    url(r'^tags/(?P<tag>\w+)$', tag, name='tags'),
]
