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
class Heroine_Reg(models.Model):
	h_name = models.CharField(max_length = 50)
	h_age = models.IntegerField()
	h_email = models.EmailField()
	h_pass = models.CharField(max_length=100)
	h_manager_name = models.CharField(max_length=100)

	def __str__(self):
		return self.h_name + " " +str(self.h_age) 
class Contact_Form(models.Model):
	gender = [('MALE','MALE'),('FEMALE','FEMALE')]
	c_name = models.CharField(max_length = 50)
	c_mobile = models.IntegerField()
	c_email = models.EmailField()
	c_gender = models.CharField(max_length=10,choices = gender)
	c_comp = models.CharField(max_length=100)

	def __str__(self):
		return self.c_name
class Com_Reg(models.Model):
	gender = [('MALE','MALE'),('FEMALE','FEMALE')]
	lang = [('TELUGU','TELUGU'),('HINDI','HINDI'),('TAMIL','TAMIL')]

	com_name = models.CharField(max_length=50)
	com_age = models.IntegerField()
	com_email = models.EmailField()
	com_nof_movies = models.IntegerField()
	com_gender = models.CharField(max_length=10,choices=gender)
	com_lang = models.CharField(max_length=10,choices=lang)
	com_mobile = models.IntegerField()

	def __str__(self):
		return self.com_name
