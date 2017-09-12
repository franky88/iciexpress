from django.db import models
from courses.models import Course
# Create your models here.
class ClassSchedule(models.Model):
	class_time = models.CharField(max_length=30)
	course=models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
	def classSchedule(self):
		class_schedule="%s (%s class)"%(self.course, self.class_time)
		return class_schedule
	def __str__(self):
		return self.classSchedule()