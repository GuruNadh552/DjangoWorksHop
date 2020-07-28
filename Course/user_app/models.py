from django.db import models

# Create your models here.
class FacultyReg(models.Model):
	gen = [('Male','Male'),('Female','Female')]
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=10)
	email = models.EmailField()
	gender = models.CharField(max_length=10,choices=gen)
	age = models.IntegerField()
	dob = models.DateField()

	def __str__(self):
		return self.name