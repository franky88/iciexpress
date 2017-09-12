from django.contrib import admin
from .models import SubjectType, Subject, Semester
# Register your models here.
admin.site.register(SubjectType)
admin.site.register(Subject)
admin.site.register(Semester)