from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from students.models import Student
from .forms import AddUserForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.db.models import Q
# Create your views here.
def studentProfile(request):
	student_profile = Student.objects.all()
	query = request.GET.get("q")
	if query:
		student_profile = Student.objects.filter(lrn=query)
	context = {
		"title": "student portal",
		"studentprofile": student_profile,
		"searchPlaceholder": "Search by LRN",
	}
	return render(request, "users/student_profile.html", context)

def instructorProfile(request, pk):
	instance = get_object_or_404(User, pk=pk)
	context = {
		"title": "instructor profile",
		"instance": instance,
	}
	return render(request, "users/instructor_profile.html", context)

def userAdd(request):
	if request.method == 'POST':
		form = AddUserForm(
			request.POST or None, 
			request.FILES or None,
			)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return redirect('bulletin:list')
	else:
		form = AddUserForm()
	context = {
		"form": form,
		"title": "registration form",
	}
	return render(request, "users/user_add.html", context)


def userLogin(request):
	next = request.GET.get('next', '/')
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user=authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(next)
			else:
				HttpResponse("Inactive user")
		else:
			return HttpResponseRedirect(settings.LOGIN_URL)
	return render(request, "users/user_login.html", {"redirect_to": next, "title": "Login"})

def userLogout(request):
	logout(request)
	return HttpResponseRedirect(settings.LOGIN_URL)
