from django.conf.urls import url
from . import views

app_name = "student"
urlpatterns = [
    url(r'^$', views.studentList, name="list"),
    url(r'^add/$', views.studentAdd, name="add"),
    url(r'^info/$', views.studentPortal, name="info"),
    url(r'^([0-9]{4})/$', views.studentYearView, name="yeararchive"),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.studentEdit, name="edit"),
    url(r'^(?P<pk>[0-9]+)/details/$', views.studentDetail, name="detail"),
]