from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Instructor
from .forms import InstructorForm
# Create your views here.
@login_required
def instructorList(request):
	instructor_list=Instructor.objects.all()
	instructor_count = Instructor.objects.count()
	query = request.GET.get("q")
	if query:
		instructor_list = instructor_list.filter(
			Q(instructor__first_name__startswith=query) |
			Q(instructor__last_name__startswith=query) |
			Q(instructor__email__startswith=query) |
			Q(employment_status__status__startswith=query) |
			Q(contact__startswith=query)
			).distinct()
	context={
		"title": "instructor list",
		"instructorlist": instructor_list,
		"searchPlaceholder": "Search instructor",
		"instructorcount": instructor_count,
	}
	return render(request, "instructor/instructor_list.html", context)
@login_required
def instructorDetail(request, pk):
	instructor_instance=get_object_or_404(Instructor, pk=pk)
	context={
		"title":"instructor details",
		"instance": instructor_instance,
	}
	return render(request, "instructor/instructor_detail.html", context)
@login_required
def instructorAdd(request):
	form = InstructorForm(request.POST or None, request.FILES or None)
	if request.method == "POST":
		if form.is_valid():
			instance=form.save(commit=False)
			instance.user = request.user
			instance.save()
			return redirect("instructor:detail", pk=instance.id)
	context = {
		"title": "add instructor",
		"form": form,
	}
	return render(request, "instructor/instructor_add.html", context)