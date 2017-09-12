from django.contrib import admin
from .models import Course, Track, Strand, Department
from subjects.models import Subject
# Register your models here.
class subjectInline(admin.TabularInline):
	model = Subject
	extra = 0
class CourseAdmin(admin.ModelAdmin):
	list_display = ["__str__", "strand", "department"]
	list_filter = ('timestamp', 'updated')
	inlines = [subjectInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Track)
admin.site.register(Strand)
admin.site.register(Department)