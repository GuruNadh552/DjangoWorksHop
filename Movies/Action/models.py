from django.db import models

# Create your models here.
class Student_Form(models.Model):
	s_name = models.CharField(max_length = 50)
	s_age = models.IntegerField()
	s_roll = models.CharField(max_length = 10)
	s_email = models.EmailField(max_length = 100)

	def __str__(self):
		return self.s_name
class Actor_Form(models.Model):
	a_name = models.CharField(max_length = 50)
	a_age = models.IntegerField()
	a_nom = models.IntegerField()

	def __str__(self):
		return self.a_name + " " + str(self.a_age) + " " + str(self.a_nom)