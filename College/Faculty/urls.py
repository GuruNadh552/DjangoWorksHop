from django.urls import path,include
from Faculty import views

urlpatterns = [
   path('display/',views.display,name="display"),
   path('FReg/',views.FReg,name="fregister"),
   path('StudentReg/',views.SReg,name="sreg"),
   path('table/<int:num>',views.table,name="table")
]