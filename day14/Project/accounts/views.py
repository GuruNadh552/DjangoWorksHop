from django.shortcuts import render,redirect
from .forms import UserForm
from django.http import HttpResponse
from django.contrib.auth import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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
			login(req,user)
		return redirect('signin')
	return render(req,'login.html')

@login_required
def signout(req):
	logout(req)
	return redirect('home')
@login_required
def profile(req):
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
			return HttpResponse('Password changesuccess')
	return render(req,'changepass.html',{'form':form})
