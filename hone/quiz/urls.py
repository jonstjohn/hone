from django.conf.urls import patterns, url

from quiz import views
from quiz.views import HomePageView, AttemptQuestionPageView, AttemptResultPageView, DetailPageView, AttemptCreateRedirectView

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^(?P<quiz_id>\d+)$', DetailPageView.as_view(), name='quiz_detail'),
    url(r'^(?P<quiz_id>\d+)/(?P<num>\d+)$', views.question, name='question'),
    url(r'^attempt/create/(?P<quiz_id>\d+)$', AttemptCreateRedirectView.as_view(), name='attempt_create'),
    url(r'^attempt/(?P<attempt_id>\d+)$', views.attempt, name='attempt'),
    url(r'^attempt/(?P<attempt_id>\d+)/(?P<num>\d+)$', AttemptQuestionPageView.as_view(), name='attempt_question'),
    url(r'^attempt/(?P<attempt_id>\d+)/result$', AttemptResultPageView.as_view(), name='attempt_result'),
)
