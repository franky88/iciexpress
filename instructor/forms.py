from django import forms
from .models import Instructor

class InstructorForm(forms.ModelForm):
	class Meta:
		model=Instructor
		fields=[
			"instructor",
			"employment_status",
			"contact",
		]