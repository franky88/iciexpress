from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class EmploymentStatus(models.Model):
	status=models.CharField(max_length=120, unique=True, default="part time")
	def __str__(self):
		return self.status.title()
class Instructor(models.Model):
	instructor=models.ForeignKey(User, on_delete=models.CASCADE)
	employment_status=models.ForeignKey(EmploymentStatus, on_delete=models.CASCADE, default=1)
	contact=models.CharField(max_length=13, blank=True)
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
	updated=models.DateTimeField(auto_now=True, auto_now_add=False)
	def __str__(self):
		return self.instructor.get_full_name().title()