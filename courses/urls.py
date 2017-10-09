from django.conf.urls import url
from . import views

app_name = "course"
urlpatterns = [
    url(r'^$', views.courseList, name="list"),
    url(r'^add/$', views.courseAdd, name="add"),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.courseEdit, name="edit"),
    url(r'^(?P<pk>[0-9]+)/details/$', views.courseDetail, name="detail"),
    # url(r'^schoolform1/(?P<pk>[0-9]+)/details/$', views.form1Detail, name="sfdetail"),
]