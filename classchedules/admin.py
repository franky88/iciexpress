from django.contrib import admin
from .models import ClassSchedule
from schedules.models import Schedule
# Register your models here.
class ClassSubjectInline(admin.TabularInline):
	model = Schedule
	extra = 1

class ClassScheduleAdmin(admin.ModelAdmin):
	list_display=['class_time', 'course']
	inlines = [ClassSubjectInline]


admin.site.register(ClassSchedule, ClassScheduleAdmin)