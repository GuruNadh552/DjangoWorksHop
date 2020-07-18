from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

x='''
	<html>
	<head>
	</head>
	<body bgcolor="red">
		<h1 style="text-align:center;font-size:300px;color:white;">GURU</h1>
	</body>
	</html>
'''

def welcome(req):
	return HttpResponse(x)

def home(req):
	return HttpResponse('<h1>This is Home Page</h1>')
def index(req,name,roll):
	return HttpResponse('<h1>This is ' + name + ' with roll '+ str(roll) + '</h1>')
def hom(req):
	return render(req,'index.html')
def register(req):
	return render(req,'myapp/register.html')