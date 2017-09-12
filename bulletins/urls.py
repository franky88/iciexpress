from django.conf.urls import url
from . import views

app_name = "bulletin"
urlpatterns = [
	url(r'^$', views.bulletinList, name='list'),
	url(r'^add/$', views.bulletinAdd, name='add'),
]