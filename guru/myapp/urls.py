from django.urls import path,include
from myapp import views
urlpatterns = [
    path('mapp/',views.home,name="home"),
    path('index/<str:name>/<int:roll>',views.index,name="index"),
    path('home/',views.hom,name="hom"),
    path('register',views.register,name="register"),
]
	