from django.db import models
from blocks.models import Block
# Create your models here.
class ClassSchedule(models.Model):
	class_time = models.CharField(max_length=30)
	block = models.ForeignKey(Block, on_delete=models.CASCADE)
	def classSchedule(self):
		class_schedule="%s (%s class)"%(self.block, self.class_time)
		return class_schedule
	def __str__(self):
		return self.classSchedule()