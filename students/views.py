from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from .models import Student, Gender
from .forms import StudentForm

# Create your views here.
@login_required
def studentList(request):
	student_list = Student.objects.all().order_by("-date_registered", "-date_updated")
	student_count = Student.objects.count()
	student_count_male = Student.objects.filter(gender__gender__startswith="male").count()
	student_count_female = Student.objects.filter(gender__gender__startswith="female").count()
	query = request.GET.get("q")
	if query:
		student_list = student_list.filter(
			Q(lrn__startswith=query) |
			Q(fname__startswith=query) |
			Q(lname__startswith=query) |
			Q(mname__startswith=query) |
			Q(ename__startswith=query) |
			Q(gender__gender__startswith=query) |
			Q(birth_date__startswith=query) |
			Q(mother_tongue__startswith=query) |
			Q(IP__startswith=query) |
			Q(religion__startswith=query) |
			Q(address__startswith=query) |
			Q(father_name__startswith=query) |
			Q(mother_name__startswith=query) |
			Q(guardian_name__startswith=query) |
			Q(relationship__startswith=query) |
			Q(contact__startswith=query) |
			Q(remarks__startswith=query) 
			).distinct()

	paginator = Paginator(student_list, 10)
	page = request.GET.get('page')
	try:
		student_list = paginator.page(page)
	except PageNotAnInteger:
		student_list = paginator.page(1)
	except EmptyPage:
		student_list = paginator.page(paginator.num_pages)
	context = {
		"title": "students",
		"studentlist": student_list,
		"searchPlaceholder": "Search students",
		"studentcount": student_count,
		"studentcountmale": student_count_male,
		"studentcountfemale": student_count_female,
	}
	return render(request, "students/student_list.html", context)
@login_required
def studentYearView(request, year):
	year_list = Student.objects.filter(date_registered__year=year)
	context = {
		"year": year,
		"yearlist": year_list,
	}
	return render(request, "students/student_year_archive.html", context)
@login_required
def studentDetail(request, pk):
	student_instance = get_object_or_404(Student, pk=pk)
	context = {
		"title": "student details",
		"instance": student_instance,
	}
	return render(request, "students/student_detail.html", context)
@login_required
# @permission_required('students.can_add')
def studentAdd(request):
	form = StudentForm(request.POST or None, request.FILES or None)
	if request.method == "POST":
		if form.is_valid():
			instance=form.save(commit=False)
			instance.user=request.user
			instance.save()
			return redirect("student:detail", pk=instance.id)
	context = {
		"title": "register student",
		"form": form,
	}
	return render(request, "students/student_add.html", context)
@login_required
# @permission_required('students.can_change')
def studentEdit(request, pk):
	instance=get_object_or_404(Student, pk=pk)
	form = StudentForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect('student:detail', pk=instance.id)
	context = {
		"form": form,
		"title": "edit student",
		"instance": instance,
	}
	return render(request, "students/student_edit.html", context)
def studentPortal(request):
	student_info = Student.objects.all()
	query = request.GET.get("q")
	if query:
		student_info = student_info.filter(
			Q(lrn__startswith=query) 
			).distinct()
	context = {
		"title": "student information",
		"studentinfo": student_info,
		"searchPlaceholder": "Search by LRN",
	}
	return render(request, "students/student_info.html", context)