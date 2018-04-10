from django.conf.urls import url
from master import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [    
    url(r'^$', views.Index_pageview.as_view(), name='index'),
    url(r'^home/$', views.Home_pageview.as_view(), name='home'), # Notice the URL has been named
    url(r'^login/$', views.Login_pageview.as_view(), name='login'),
    url(r'^dashboard/$', views.Dashboard_pageview.as_view(), name='dashboard'),
    ]