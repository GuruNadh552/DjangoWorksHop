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
