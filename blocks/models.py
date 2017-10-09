from django.db import models
from instructor.models import Instructor
from classchedules.models import ClassSchedule
# Create your models here.
# class GradeLevel(models.Model):
# 	level=models.CharField(max_length=2, default="")
# 	def __str__(self):
# 		return self.level
class Level(models.Model):
	level = models.CharField(max_length=2, default="")
	def __str__(self):
		return self.level
class Block(models.Model):
	instructor=models.ForeignKey(Instructor, on_delete=models.CASCADE)
	block_name=models.CharField(max_length=60, unique=True)
	grade_level=models.ForeignKey(Level, on_delete=models.CASCADE)
	class_schedule=models.ForeignKey(ClassSchedule, on_delete=models.CASCADE, default=1)
	timestamp=models.DateField(auto_now=False, auto_now_add=True)
	updated=models.DateField(auto_now=True, auto_now_add=False)
	def __str__(self):
		return self.block_name.title()