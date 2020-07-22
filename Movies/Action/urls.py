from django.urls import path,include
from Action import views

urlpatterns = [
    path('index/', views.index,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('register/',views.register,name="register"),
]
