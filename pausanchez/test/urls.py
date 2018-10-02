# coding=utf-8
from django.conf.urls import url

from . import views

'''
This file enables us to write friendly browser URLs.
It is similar to what can be done in .htaccess file in an apache server
'''

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^publications$', views.publications, name='publications'),
    url(r'^remove_publication', views.remove_publication, name='remove_publication'),
]