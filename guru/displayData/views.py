from django.shortcuts import render


# Create your views here.
def showdata(req):
	info = {
		"name" : "Gurunadh",
		"roll" : "S160552" ,
		"Age" : 19
	}
	return render(req,'navbar/showdata.html')