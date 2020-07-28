from django.contrib import admin
from django.urls import path,include
from image_upload import views

urlpatterns = [
	path('display/',views.display,name="display"),
	path('index/',views.index,name="index")
]

