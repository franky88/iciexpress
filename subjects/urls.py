from django.conf.urls import url
from . import views

app_name = "subject"
urlpatterns = [
    url(r'^$', views.subjectList, name="list"),
    url(r'^add/$', views.subjectAdd, name="add"),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.subjectEdit, name="edit"),
    url(r'^(?P<pk>[0-9]+)/details/$', views.subjectDetail, name="detail"),
]