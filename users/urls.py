from django.conf.urls import url
from . import views

app_name = "user"
urlpatterns = [
	url(r'^add/$', views.userAdd, name="add"),
	url(r'^login/$', views.userLogin, name='login'),
	url(r'^logout/$', views.userLogout, name='logout'),
	url(r'^profile/student/$', views.studentProfile, name="studentprofile"),
	url(r'^(?P<pk>[0-9]+)/profile/instructor$', views.instructorProfile, name="instructorprofile"),
]