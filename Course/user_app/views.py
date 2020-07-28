from django.shortcuts import render
from django.http import HttpResponse
from .forms import FacultyForm
from .models import *
from django.core.mail import EmailMessage
from Course import settings
# Create your views here.

def FacRegister(req):
	form = FacultyForm()
	if(req.method == 'POST'):
		form = FacultyForm(req.POST)
		if (form.is_valid()):
			form.save()

			#For sending Email Purpose

			name = form.data['name']
			email = form.data['email']
			sub = 'Reg : Registration of Course Website '
			body = 'Hi '+ name +'! You are Registrated Successfully ......'
			sender = settings.EMAIL_HOST_USER

			email_msg = EmailMessage(sub,body,sender,[email])
			email_msg.send()

			return HttpResponse('SUccess')

	return render(req,'facultyreg.html',{'form':form})
