from django.db import models
from blocks.models import Block
from students.models import Student
# Create your models here.
class ClassRoster(models.Model):
	block=models.ForeignKey(Block, on_delete=models.CASCADE, default=1)
	student=models.ForeignKey(Student, on_delete=models.CASCADE, default=1)
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
	updated=models.DateTimeField(auto_now=True, auto_now_add=False)
	def __str__(self):
		return self.block.block_name.upper()
