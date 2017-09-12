from django.conf.urls import url
from . import views

app_name = "block"
urlpatterns = [
    url(r'^$', views.blockList, name="list"),
    url(r'^add/$', views.blockAdd, name="add"),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.blockEdit, name="edit"),
    url(r'^(?P<pk>[0-9]+)/details/$', views.blockDetail, name="detail"),
    url(r'^schoolform1/(?P<pk>[0-9]+)/details/$', views.form1Detail, name="sfdetail"),
]