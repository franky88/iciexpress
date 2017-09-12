from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .forms import CourseForm
from .models import Course
# Create your views here.
def courseList(request):
	course_list = Course.objects.all()
	context = {
		"title": "courses offered",
		"courselist": course_list,
	}
	return render(request, "courses/course_list.html", context)

def courseAdd(request):
	form = CourseForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			instance=form.save(commit=False)
			instance.user=request.user
			instance.save()
			return redirect("course:list")
	context = {
		"title": "add course",
		"form": form,
	}
	return render(request, "courses/course_add.html", context)

@permission_required('blocks.can_change')
def courseEdit(request, pk):
	instance=get_object_or_404(Course, pk=pk)
	form = CourseForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect('course:list')
	context = {
		"form": form,
		"title": "edit course",
		"instance": instance,
	}
	return render(request, "courses/course_edit.html", context)