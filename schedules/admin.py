from django.contrib import admin
from .models import Schedule, Day, Room
# Register your models here.
admin.site.register(Schedule)
admin.site.register(Day)
admin.site.register(Room)