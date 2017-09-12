from django.contrib import admin
from .models import Instructor, EmploymentStatus
# Register your models here.
class InstructorAdmin(admin.ModelAdmin):
	list_filter = ['employment_status']

admin.site.register(Instructor, InstructorAdmin)
admin.site.register(EmploymentStatus)