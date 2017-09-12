from django.db import models

# Create your models here.
class Branch(models.Model):
	school_name=models.CharField(max_length=120, unique=True)
	school_id=models.CharField(max_length=6, unique=True)
	def __str__(self):
		return self.school_name
class SchoolYear(models.Model):
	branch=models.ForeignKey(Branch, on_delete=models.CASCADE)
	year_start=models.CharField(max_length=4)
	year_end=models.CharField(max_length=4)
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
	updated=models.DateTimeField(auto_now=True, auto_now_add=False)
	def sy(self):
		sy="%s - %s"%(self.year_start, self.year_end)
		return sy
	def __str__(self):
		return self.sy()