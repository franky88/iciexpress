from django import forms
from django.contrib.auth.models import User

class AddUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			"email",
			"username",
			"password",
			"first_name",
			"last_name",
		]