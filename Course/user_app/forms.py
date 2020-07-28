from django.forms import ModelForm
from .models import FacultyReg

class FacultyForm(ModelForm):
	class Meta:
		model = FacultyReg
		fields = '__all__'