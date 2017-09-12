from io import BytesIO
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import Block
from .forms import BlockForm
# Create your views here.
@login_required
def blockList(request):
	block_list=Block.objects.all().order_by("-id")
	context={
		"title": "block list",
		"blocklist": block_list,
	}
	return render(request, "blocks/block_list.html", context)
@login_required
def blockDetail(request, pk):
	instance=get_object_or_404(Block, pk=pk)
	context = {
		"title": "block details",
		"instance": instance,
	}
	return render(request, "blocks/block_detail.html", context)
@login_required
# @permission_required('blocks.can_add')
def blockAdd(request):
	form = BlockForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			instance=form.save(commit=False)
			instance.user=request.user
			instance.save()
			return redirect("block:list")
	context = {
		"title": "add block",
		"form": form,
	}
	return render(request, "blocks/block_add.html", context)
@login_required
# @permission_required('blocks.can_change')
def blockEdit(request, pk):
	instance=get_object_or_404(Block, pk=pk)
	form = BlockForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect('block:list')
	context = {
		"form": form,
		"title": "edit block",
		"instance": instance,
	}
	return render(request, "blocks/block_edit.html", context)
@login_required
def form1Detail(request, pk):
	instance=get_object_or_404(Block, pk=pk)
	context = {
		"title": "school form 1",
		"instance": instance,
	}
	return render(request, "blocks/schoolform1_detail.html", context)