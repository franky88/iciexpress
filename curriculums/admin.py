from django.contrib import admin
from .models import Curriculum
from subjects.models import Subject
# Register your models here.
class CurriculumInline(admin.TabularInline):
	model = Subject
	extra = 1

class CurriculumAdmin(admin.ModelAdmin):
	list_display = ['cur_name']
	inlines=[CurriculumInline]


admin.site.register(Curriculum, CurriculumAdmin)