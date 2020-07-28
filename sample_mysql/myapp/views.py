from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from sample_mysql import settings
from django.core.mail import EmailMessage
import random,string
# Create your views here.

def register(req):
	form = Reg_Form
	if(req.method=='POST'):
		form = Reg_Form(req.POST)
		if form.is_valid():
			uname = req.POST['User_Name']
			fname = req.POST['First_Name']
			lname = req.POST['Last_Name']
			phone = req.POST['Mobile']
			mail = req.POST['Email_Id']
			password = ''.join(random.choices(string.ascii_lowercase+string.digits,k=8))
			data = Register_Form(User_Name=uname,First_Name=fname,Last_Name=lname,Mobile=phone,Email_Id=mail,Password=password)
			data.save()
			#messages.success("You are Registerd Successfully")
		
		'''name = fname + lname
		email = mail
		sub = 'Reg : Registration of Course Website '
		body = 'Hi '+ name +'! You are Registrated Successfully ...... <br> Your Password is '+password
		sender = settings.EMAIL_HOST_USER
		email_msg = EmailMessage(sub,body,sender,[email])
		email_msg.send()'''
		return redirect('login')
	return render(req,'register.html',{'form':form})
def login(req):
	if(req.method=='POST'):
		uname = req.POST['user']
		password = req.POST['pass']

		try:
			data = Register_Form.objects.get(User_Name=uname)
			if(data.Password == password):
				return HttpResponse('Login Successfully')
			return HttpResponse('Invalid credentials')
		except Exception as e:
			return HttpResponse('User name not Found')
	return render(req,'login.html')