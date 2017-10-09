from django.contrib import admin
from .models import Curriculum
from subjects.models import Subject
# Register your models here.

class CurriculumAdmin(admin.ModelAdmin):
	list_display = ['cur_name']


admin.site.register(Curriculum, CurriculumAdmin)