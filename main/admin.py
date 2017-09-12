from django.contrib import admin
from .models import SchoolYear, Branch
# Register your models here.
class SchoolYearAdmin(admin.ModelAdmin):
	list_display=["__str__", "year_start", "year_end", "branch"]


admin.site.register(SchoolYear, SchoolYearAdmin)
admin.site.register(Branch)