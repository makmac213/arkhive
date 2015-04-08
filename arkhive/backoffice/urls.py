from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# backoffice
from .views import BackofficeView, BackofficeNews

urlpatterns = patterns('',
    
    # dashboard
    url(r'^$', BackofficeView.Dashboard.as_view(), 
                        name='backoffice_dashboard'),


    # news
    url(r'^news/$', BackofficeNews.Manage.as_view(), 
                        name='news_manage'),
    url(r'^news/(?P<id>.*)/$', BackofficeNews.Display.as_view(), 
                        name='news_display'),


)