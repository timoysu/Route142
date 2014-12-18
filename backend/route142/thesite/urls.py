from django.conf.urls import patterns, url

from thesite.views import IndexView, InfoQueryView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
    url(r'^query/$', InfoQueryView.as_view()),
)