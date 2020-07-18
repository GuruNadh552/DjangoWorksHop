from django.urls import path
from displayData import views

urlpatterns = [
	path('showdata/',views.showdata,name="showdata");
]