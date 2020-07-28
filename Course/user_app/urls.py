from django.urls import path,include
from user_app import views

urlpatterns = [
    path('faculty/register',views.FacRegister,name="FacRegister"),
]