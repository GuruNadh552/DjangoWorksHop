from django.shortcuts import render,redirect
from django.http import HttpResponse
from Action.models import *
def index(req):
	return render(req,'index.html')
def about(req):
	return render(req,'about.html')
def contact(req):
		if (req.method == "POST"):
			name = req.POST['name']
			mobile = req.POST['mobile']
			email = req.POST['email']
			gender = req.POST['gender']
			com = req.POST['comp']

			data = Contact_Form(c_name = name,c_mobile = mobile,c_email = email,c_gender=gender,c_comp = com)
			data.save()
			return render(req,'index.html')

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
		return HttpResponse('<script type="text/javascript">alert("... Data Added Successfully ...")</script>')
	return render(req,'register.html')

def showdata(req):
	data = Contact_Form.objects.all()
	return render(req,'showdata.html',{'data':data})

def delete(req,id):
	data = Contact_Form.objects.get(id=id)
	data.delete()
	return redirect('showdata')
def edit(req,id):
	data = Contact_Form.objects.get(id=id)
	return render(req,'update.html',{'data':data})
def update_data(req,id):
	if (req.method == "POST"):
			name = req.POST['name']
			mobile = req.POST['mobile']
			email = req.POST['email']
			gender = req.POST['gender']
			com = req.POST['comp']
	data = Contact_Form.objects.filter(id=id).update(c_name = name,c_mobile = mobile,c_email = email,c_gender=gender,c_comp = com)

	return redirect('showdata')


def comedian_reg(req):
	if(req.method=="POST"):
		name = req.POST['name']
		age = req.POST['age']
		email = req.POST['email']
		nof = req.POST['nof_movies']
		gender = req.POST['gender']
		lang = req.POST['lang']
		mobile = req.POST['mobile']

		data = Com_Reg(com_name = name,com_age = age,com_email = email,com_nof_movies = nof,com_gender = gender,com_lang = lang,com_mobile = mobile)
		data.save()

		return render(req,'index.html')
	return render(req,'comedian_reg.html')

def show_comdata(req):
	data = Com_Reg.objects.all()
	return render(req,'com_showdata.html',{"data":data})

def com_update(req,id):
	if(req.method=="POST"):
		name = req.POST['name']
		age = req.POST['age']
		email = req.POST['email']
		nof = req.POST['nof_movies']
		gender = req.POST['gender']
		lang = req.POST['lang']
		mobile = req.POST['mobile']
	data = Com_Reg.objects.filter(id=id).update(com_name = name,com_age = age,com_email = email,com_nof_movies = nof,com_gender = gender,com_lang = lang,com_mobile = mobile)
	
	return redirect('com_showdata')
def com_edit(req,id):
	data = Com_Reg.objects.get(id=id)
	return render(req,'com_update.html',{"data":data})

def com_delete(req,id):
	data = Com_Reg.objects.get(id=id)
	data.delete()
	return redirect('com_showdata')