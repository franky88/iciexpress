from django.conf.urls import url
from . import views

app_name = "instructor"
urlpatterns = [
    url(r'^$', views.instructorList, name="list"),
    url(r'^add/$', views.instructorAdd, name="add"),
    url(r'^(?P<pk>[0-9]+)/details/$', views.instructorDetail, name="detail"),
]