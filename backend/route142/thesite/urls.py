from django.conf.urls import patterns, url

from thesite.views import IndexView, InfoQueryView, NearPointsView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
    url(r'^query/$', InfoQueryView.as_view()),
    url(r'^near-points/$', NearPointsView.as_view())
)