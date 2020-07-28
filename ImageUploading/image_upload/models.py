from django.db import models

# Create your models here.

class Upload(models.Model):
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=10)
	image = models.ImageField(upload_to='static/images')

	def __str__(self):
		return self.name