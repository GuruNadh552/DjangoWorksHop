from django.shortcuts import render
from django.http import HttpResponse
from Action.models import *
def index(req):
	return render(req,'index.html')
def about(req):
	return render(req,'about.html')
def contact(req):
	return render(req,'contact.html')
def register(req):
	if (req.method == "POST"):
		name = req.POST['act_name']
		age = req.POST['act_age']
		email = req.POST['act_email']
		password = req.POST['act_pass']
		manager = req.POST['act_manager']

		data = Heroine_Reg(h_name=name , h_age=age,h_email=email,h_pass=password,h_manager_name=manager)
		data.save()
		return HttpResponse('Success')
	return render(req,'register.html')