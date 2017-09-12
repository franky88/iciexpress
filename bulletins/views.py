from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Article
from .forms import ArticleForm
# Create your views here.
def bulletinList(request):
	article_list=Article.objects.all().order_by("-timestamp")
	reporter = User.objects.all().order_by()
	context = {
		"title": "school bulletin",
		"articlelist": article_list,
		"reporterlist": reporter,
	}
	return render(request, "bulletins/bulletin_list.html", context)
def bulletinAdd(request):
	form = ArticleForm(request.POST or None, request.FILES or None)
	if request.method == "POST":
		if form.is_valid():
			instance=form.save(commit=False)
			instance.user = request.user
			instance.save()
			return redirect("bulletin:list")
	context = {
		"title": "add article",
		"form": form,
	}
	return render(request, "bulletins/bulletin_add.html", context)