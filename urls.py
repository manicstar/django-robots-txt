from django.conf.urls.defaults import patterns, include, url

from robotstxt.views import TextView

urlpatterns = patterns('',
    url(
        r'^robots.txt$',
        TextView.as_view(template_name = 'robots.txt'),
    ),
)
