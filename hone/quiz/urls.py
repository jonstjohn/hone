from django.conf.urls import patterns, url

from quiz import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<quiz_id>\d+)/(?P<num>\d+)$', views.question, name='question'),
)
