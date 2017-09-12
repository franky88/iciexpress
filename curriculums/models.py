from django.db import models
from courses.models import Course
# Create your models here.
class Curriculum(models.Model):
	cur_name = models.CharField(max_length=120, unique=True, default="anim2017")
	course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
	def __str__(self):
		return self.cur_name.title()
