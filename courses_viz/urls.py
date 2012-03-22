from django.conf.urls.defaults import patterns, include, url

from courses_viz import views

urlpatterns = patterns('',
    url(r'^bubbles/$', views.render_template, {'template': 'bubble.html'}, name='bubble'),
    url(r'^timelines/$', views.render_template, {'template': 'timelines.html'}, name='timelines'),
)
