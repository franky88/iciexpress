from django.db import models
from subjects.models import Subject
from instructor.models import Instructor
from students.models import Student
from classchedules.models import ClassSchedule
# Create your models here.
class Day(models.Model):
	day=models.CharField(max_length=10, unique=True)
	def __str__(self):
		return self.day
class Room(models.Model):
	room=models.CharField(max_length=60, default="Lecture Room 1")
	def __str__(self):
		return self.room

class Schedule(models.Model):
	start_time=models.TimeField()
	end_time=models.TimeField()
	day=models.ForeignKey(Day, on_delete=models.CASCADE)
	instructor=models.ForeignKey(Instructor, on_delete=models.CASCADE)
	subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
	room=models.ForeignKey(Room, on_delete=models.CASCADE, default=1)
	class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE, default=1)
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
	updated=models.DateTimeField(auto_now=True, auto_now_add=False)
	def __str__(self):
		subin="%s (%s - %s)"%(self.subject, self.start_time, self.end_time)
		return subin