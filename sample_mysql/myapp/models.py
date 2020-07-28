from django.db import models

# Create your models here.
class Register_Form(models.Model):
	First_Name  = models.CharField(max_length=100)
	Last_Name = models.CharField(max_length=100)
	User_Name = models.CharField(max_length=100,unique=True) # Unique for Single Username 
	Password = models.CharField(max_length=100)
	Email_Id = models.EmailField()
	Mobile = models.CharField(max_length=10)

	def __str__(self):
		return self.User_Name
