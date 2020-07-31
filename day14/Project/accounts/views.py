from django.shortcuts import render,redirect
from .forms import UserForm
from django.http import HttpResponse
from django.contrib.auth import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import csv
# Create your views here.

def home(req):
	return render(req,'home.html')
def signup(req):
	form = UserForm()
	if(req.method=='POST'):
		form = UserForm(req.POST)
		if (form.is_valid()):
			form.save()
		return redirect('signin')
	return render(req,'register.html',{'form':form})
def signin(req):
	if (req.method=='POST'):
		username = req.POST['username']
		password = req.POST['password']
		user = authenticate(username=username,password=passw)
		if(user is not None):
			messages.success(req,'SuccessFully Login')
			login(req,user)
		else:
			messages.warning(req,'Invalid Credentials')
			return redirect('signin')
	return render(req,'login.html')

@login_required
def signout(req):
	logout(req)
	return redirect('home')
@login_required
def profile(req):
	messages.success(req,'SuccessFully Login')
	user = get_user(req)
	return render(req,'profile.html',{'user':user})
@login_required
def changepass(req):
	form = PasswordChangeForm(req.user)
	if (req.method=='POST'):
		form = PasswordChangeForm(req.user,req.POST)
		if (form.is_valid()):
			u = form.save()
			update_session_auth_hash(req,u)
			return redirect('csuccess')
	return render(req,'changepass.html',{'form':form})

def changesu(req):
	logout(req)
	return render(req,'csuccess.html')

def showusers(req):
	data = User.objects.all()
	return render(req,'showusers.html',{'data':data})
@login_required
def edituser(req,id):
	user = User.objects.get(id=id)
	if (req.method=='POST'):
		first_name = req.POST['first_name']
		last_name = req.POST['last_name']
		username = req.POST['username']
		email = req.POST['email']
		user.first_name = first_name
		user.last_name = last_name
		user.email = email
		user.username = username
		user.save()
		messages.success(req,'%s is updated SuccessFully'%(username))
		return redirect('showusers')
	return render(req,'edituser.html',{'data':user})
def deleteuser(req,id):
	user = User.objects.get(id=id)
	if (req.method=='POST'):
		user = User.objects.get(id=id)
		messages.success(req,'%s deleted SuccessFully'%(user.username))
		user.delete()
		return redirect('showusers')
	return render(req,'deleteuser.html',{'user':user})

def savedata(req):
	resp = HttpResponse(content_type="text/csv")
	writer = csv.writer(resp)
	writer.writerow(['ID','FIRST_NAME','LAST_NAME','EMAIL','USERNAME','LAST_LOGIN','DATE_JOINED'])

	for i in User.objects.all().values_list('id','first_name','last_name','email','username','last_login','date_joined'):
		writer.writerow(i)
	resp['Content-Disposition'] = 'attachments; filename="data.csv"'
	return resp


