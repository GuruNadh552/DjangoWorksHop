from django.forms import ModelForm
from image_upload.models import Upload

class UploadForm(ModelForm):
	class Meta:
		model = Upload
		fields = '__all__'
