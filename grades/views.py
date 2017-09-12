from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Grade
from students.models import Student
# Create your views here.
@login_required
def gradeList(request):
	student_list = Student.objects.all().order_by("-date_registered", "-date_updated")
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
		"title": "student grades",
		"gradelist": student_list,
		"searchPlaceholder": "Search grades",
	}
	return render(request, "grades/grade_list.html", context)
@login_required
def gradeDetail(request, pk):
	grade_instance = get_object_or_404(Student, pk=pk)
	context = {
		"title": "grade details",
		"instance": grade_instance,
	}
	return render(request, "grades/grade_detail.html", context)