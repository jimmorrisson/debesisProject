"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from .views import *

urlpatterns = [
    # localhost/workers
    url(r'^$', emp_list, name='list'),
    # localhost/workers/create
    url(r'^create/$', emp_create, name='create'),
    # localhost/1
    url(r'^(?P<id>\d+)/$', emp_details, name='detail'),
    # localhost/1/edit
    url(r'^(?P<id>\d+)/edit/$', emp_update, name='update'),
    # localhost/1/delete
    url(r'^(?P<id>\d+)/delete/$', emp_delete),
    # /jobposition/add
    # url(r'^/employers/(?P<slug>[\w-]+)/$', emp_details, name='details'),
    # url(r'^jobposition/add/$', views.JobPositionCreate.as_view(), name='jobPosition-add'),

]
