from django.contrib import admin
from .models import Student, Gender, StudentStatus
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	date_hierarchy = 'date_registered'
	list_filter = ['date_registered', 'date_updated']
	list_display = ['__str__', 'mname', 'ename', 'course']


admin.site.register(Student, StudentAdmin)
admin.site.register(Gender)
admin.site.register(StudentStatus)