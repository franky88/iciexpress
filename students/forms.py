from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = (
				"lrn",
				"fname",
				"lname",
				"mname",
				"ename",
				"gender",
				"birth_date",
				"mother_tongue",
				"IP",
				"religion",
				"address",
				"image",
				"father_name",
				"mother_name",
				"guardian_name",
				"relationship",
				"contact",
				"remarks",
				"block",
				"course",
			)