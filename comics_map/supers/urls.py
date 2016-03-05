from django.conf.urls import url

from . import views

app_name = 'supers'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<supers_name>)/$', views.detail, name='detail'),
	url(r'^add_super/$', views.add_super, name='add_super'),
	url(r'^add_city/$', views.add_irl_city, name='add_city'),
	url(r'^big_bang/$', views.big_bang, name='big_bang')
]