from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from .models import Subject
from .forms import SubjectForm
# Create your views here.
@login_required
def subjectList(request):
	subject_list = Subject.objects.all().order_by("-id")
	query = request.GET.get("q")
	if query:
		subject_list = subject_list.filter(
			Q(subject_type__subject_type__startswith=query) |
			Q(subject_code__startswith=query) |
			Q(descriptive_title__icontains=query) |
			Q(units__startswith=query) |
			Q(hours__startswith=query) |
			Q(fee__startswith=query) 
			).distinct()

	paginator = Paginator(subject_list, 10)
	page = request.GET.get('page')
	try:
		subject_list = paginator.page(page)
	except PageNotAnInteger:
		subject_list = paginator.page(1)
	except EmptyPage:
		subject_list = paginator.page(paginator.num_pages)
	context = {
		"title": "subjects",
		"subjectlist": subject_list,
		"searchPlaceholder": "Search subject",
	}
	return render(request, "subjects/subject_list.html", context)
@login_required
def subjectDetail(request, pk):
	subject_instance = get_object_or_404(Subject, pk=pk)
	context = {
		"title": "subject details",
		"instance": subject_instance,
	}
	return render(request, "subjects/subject_detail.html", context)
@login_required
@permission_required('subjects.can_add')
def subjectAdd(request):
	form = SubjectForm(
		request.POST or None,
		)
	if request.method == "POST":
		if form.is_valid():
			instance=form.save(commit=False)
			instance.save()
			return redirect("subject:detail", pk=instance.id)
	context = {
		"title": "register subject",
		"form": form,
	}
	return render(request, "subjects/subject_add.html", context)
@login_required
@permission_required('subjects.can_change')
def subjectEdit(request, pk):
	instance=get_object_or_404(Subject, pk=pk)
	form = SubjectForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect('subject:list')
	context = {
		"form": form,
		"title": "edit subject",
		"instance": instance,
	}
	return render(request, "subjects/subject_edit.html", context)