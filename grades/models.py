from django.db import models
from students.models import Student
from subjects.models import Subject
from instructor.models import Instructor
# Create your models here.
class Quarter(models.Model):
	quarter=models.CharField(max_length=2, unique=True)
	def __str__(self):
		return self.quarter
class Grade(models.Model):
	student=models.ForeignKey(Student, on_delete=models.CASCADE)
	subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
	instructor=models.ForeignKey(Instructor, on_delete=models.CASCADE)
	quarter=models.ForeignKey(Quarter, on_delete=models.CASCADE, default=1)
	grade=models.IntegerField()
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
	updated=models.DateTimeField(auto_now=True, auto_now_add=False)
	def __str__(self):
		sg="%s - %s (Quarter %s)"%(self.student, self.subject, self.quarter)
		return sg