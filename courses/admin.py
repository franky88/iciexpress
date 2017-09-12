from django.contrib import admin
from .models import Course, Track, Strand, Department
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
	list_display = ["__str__", "strand", "department"]
	list_filter = ('timestamp', 'updated')


admin.site.register(Course, CourseAdmin)
admin.site.register(Track)
admin.site.register(Strand)
admin.site.register(Department)