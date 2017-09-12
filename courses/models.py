from django.db import models
# Create your models here.
class Track(models.Model):
	track_name=models.CharField(max_length=120, unique=True)
	def __str__(self):
		return self.track_name.upper()
class Strand(models.Model):
	track=models.ForeignKey(Track, on_delete=models.CASCADE)
	strand_name=models.CharField(max_length=120, unique=True)
	def __str__(self):
		return self.strand_name.upper()
class Department(models.Model):
	department_name=models.CharField(max_length=120, unique=True)
	def __str__(self):
		return self.department_name.upper()
class Course(models.Model):
	strand=models.ForeignKey(Strand, on_delete=models.CASCADE)
	department=models.ForeignKey(Department, on_delete=models.CASCADE)
	course_name=models.CharField(max_length=120)
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
	updated=models.DateTimeField(auto_now=True, auto_now_add=False)
	def __str__(self):
		return self.course_name.upper()