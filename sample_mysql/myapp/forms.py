from django.forms import ModelForm
from .models import *

class Reg_Form(ModelForm):
	class Meta:
		model = Register_Form
		fields = ['First_Name' , 'Last_Name',  'User_Name' ,'Email_Id', 'Mobile' ]