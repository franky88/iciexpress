from django.db import models
from curriculums.models import Curriculum
# Create your models here.
class Semester(models.Model):
	semester=models.CharField(max_length=12)
	def __str__(self):
		return self.semester
class SubjectType(models.Model):
	subject_type=models.CharField(max_length=120, unique=True)
	def __str__(self):
		return self.subject_type
class Subject(models.Model):
	subject_type=models.ForeignKey(SubjectType, on_delete=models.CASCADE)
	semester=models.ForeignKey(Semester, on_delete=models.CASCADE)
	curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE, default=1)
	subject_code=models.CharField(max_length=20, unique=True)
	descriptive_title=models.CharField(max_length=255)
	subject_description=models.TextField(default="", blank=True)
	units=models.IntegerField()
	hours=models.IntegerField()
	fee=models.FloatField()
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
	updated=models.DateTimeField(auto_now=True, auto_now_add=False)
	def __str__(self):
		return self.descriptive_title.upper()