from django.urls import path,include
from Action import views

urlpatterns = [
    path('index/', views.index,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('register/',views.register,name="register"),
    path('showdata/',views.showdata,name="showdata"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('update_data/<int:id>',views.update_data,name = "update_data"),
   
    path('comedian_reg/',views.comedian_reg,name="comedian_reg"),
    path('show_comdata',views.show_comdata,name="com_showdata"),
    path('com_edit/<int:id>',views.com_edit,name="com_edit"),
    path('com_delete/<int:id>',views.com_delete,name="com_delete"),
    path('com_update/<int:id>',views.com_update,name="com_update"),
]
