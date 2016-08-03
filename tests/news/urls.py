
from django.conf.urls import patterns, url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),    
	url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^base_login/$', views.login_view),
    url(r'^news/(?P<pk>\d+)$', views.about, name='about'),


]