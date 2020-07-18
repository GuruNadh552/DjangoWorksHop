from django.urls import path,include
from Faculty import views

urlpatterns = [
   path('display/',views.display)
]