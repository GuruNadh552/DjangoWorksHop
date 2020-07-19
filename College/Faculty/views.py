from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display(req):
	info = {
		"name" : "GURUNADH",
		"roll" : "S160552",
		"age" : "18"
	}
	return render(req,'Faculty/showdata.html',{'data':info})
def FReg(req):
	if (req.method=="POST"):
		name = req.POST['name']
		email = req.POST['email']
		ID = req.POST['id']
		age = req.POST['age']
		info = {
			'name' : name,
			'email': email,
			'ID' :ID,
			'Age' : age
		}
		return render(req,'Faculty/success.html',{'data':info})
	return render(req,'Faculty/FacultyReg.html')
def SReg(req):
	if req.method=="POST":
		name = req.POST['name']
		password = req.POST['password']
		email = req.POST['email']
		if (name == password):
			return HttpResponse('<h1> Welcome ' + name + '</h1>')
		else:
			return HttpResponse('<h1>Invalid Credentials</h1>')
	return render(req,'Faculty/StudentReg.html')

def table(req,num):
	x=[]
	for i in range(1,11):
		x.append(str(num) +' X ' + str(i) + " = " + str(num*i))
	return render(req,'Faculty/table.html',{'data':x})