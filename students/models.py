from datetime import date
from django.db import models
from django.contrib.auth.models import User
from blocks.models import Block
from courses.models import Course
# Create your models here.
class StudentStatus(models.Model):
	status=models.CharField(max_length=120, default="regular")
	def __str__(self):
		return self.status.upper()
class Gender(models.Model):
	gender=models.CharField(max_length=6, default="male")
	def __str__(self):
		return self.gender

def image_upload_location(instance, filename):
	return 'user_{0}/{1}'.format(instance.id, filename)

class Student(models.Model):
	lrn=models.CharField(max_length=12, unique=True)
	fname=models.CharField(max_length=60, verbose_name="first name", default="")
	lname=models.CharField(max_length=60, verbose_name="last name", default="")
	mname=models.CharField(max_length=60, blank=True, verbose_name="middle name")
	ename=models.CharField(max_length=5, blank=True, verbose_name="extension name")
	gender=models.ForeignKey(Gender, on_delete=models.CASCADE, default=1)
	birth_date=models.DateField(help_text="Date format yyyy-mm-dd, e.g 2000-01-20.")
	mother_tongue=models.CharField(max_length=60, default="bisaya")
	IP=models.CharField(max_length=60, help_text="Ethnic group", default="higaonon")
	religion=models.CharField(max_length=60, default="roman catholic")
	address=models.TextField(default="--student address--", help_text="Format: house#/Street/Sitio/Purok, Barangay, Municipality/City, Province")
	image=models.ImageField(upload_to=image_upload_location, blank=True)
	father_name=models.CharField(max_length=120, help_text="Format: (Last Name, First Name, Middle Name)", default="--father's name of student--", verbose_name="father's name")
	mother_name=models.CharField(max_length=120, help_text="Format: (Last Name, First Name, Middle Name)", default="--mother's name of student--", verbose_name="mother's name")
	guardian_name=models.CharField(max_length=160, help_text="Full name of guardian", blank=True, verbose_name="guardian's name")
	relationship=models.CharField(max_length=120, blank=True)
	contact=models.CharField(max_length=13, help_text=" contact number of parents or guardian", blank=True)
	remarks=models.CharField(max_length=60, default="", help_text="", blank=True)
	date_registered=models.DateTimeField(auto_now=False, auto_now_add=True)
	date_updated=models.DateTimeField(auto_now=True, auto_now_add=False)
	block=models.ForeignKey(Block, on_delete=models.CASCADE, default=1)
	course=models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
	def full_name(self):
		if self.mname and self.ename:
			fullname="%s %s, %s %s."%(self.lname, self.ename, self.fname, self.mname[0])
			return fullname
		elif not self.mname:
			fullname="%s %s, %s"%(self.lname, self.ename, self.fname)
			return fullname
		elif not self.ename:
			fullname="%s, %s %s."%(self.lname, self.fname, self.mname[0])
			return fullname
		else:
			fullname="%s, %s"%(self.lname, self.fname)
			return fullname
	def __str__(self):
		return self.full_name()
	def getAge(self):
		today=date.today()
		return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))