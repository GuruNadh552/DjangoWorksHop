from django.shortcuts import render
from django.http import HttpResponse
from .models import Upload
from .forms import UploadForm

# Create your views here.
def index(req):
	form = UploadForm()
	if req.method=='POST':
		form = UploadForm(req.POST,req.FILES)
		if (form.is_valid()):
			form.save()
			return HttpResponse('SuccessFully Uploaded')
	return render(req,'index.html',{'data':form})
def display(req):
	data = Upload.objects.all()
	return render(req,'display.html',{'data':data})