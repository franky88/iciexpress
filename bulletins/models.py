from django.db import models
from django.contrib.auth.models import User
# Create your models here.
def upload_location(instance, filename):
	return 'reporter_{0}/{1}'.format(instance.id, filename)

class Article(models.Model):
	headline=models.CharField(max_length=200)
	content=models.TextField(blank=True)
	image=models.ImageField(upload_to=upload_location, blank=True)
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
	updated=models.DateTimeField(auto_now=True, auto_now_add=False)
	def __str__(self):
		return self.headline