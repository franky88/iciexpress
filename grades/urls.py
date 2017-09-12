from django.conf.urls import url
from . import views

app_name = "grade"
urlpatterns = [
    url(r'^$', views.gradeList, name="list"),
    url(r'^(?P<pk>[0-9]+)/details/$', views.gradeDetail, name="detail"),
]