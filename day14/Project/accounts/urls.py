from accounts import views
from django.urls import path,include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home,name="home"),
    path('signup/', views.signup,name="signup"),
    #path('signin/', views.signin,name="signin"),
   # path('signout/', views.signout,name="signout"),
   path('signin/',auth_views.LoginView.as_view(template_name='login.html'),name="signin"),
   path('signout/',auth_views.LogoutView.as_view(template_name='logout.html'),name="signout"),
   path('profile/',views.profile,name="profile"),
   path('changepass/',views.changepass,name="changepass"),
   path('changesu/',views.changesu,name="csuccess"),
   path('showusers/',views.showusers,name="showusers"),
   path('edituser/<int:id>',views.edituser,name="edituser"),
   path('deleteuser/<int:id>',views.deleteuser,name="deleteuser"),
   path('savedata/',views.savedata,name="savedata"),
]
