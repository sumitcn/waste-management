from django.urls import path , include
from . import views


app_name='account'

urlpatterns=[
  
  path('logout/',views.logoutview,name='logout'),
    path('anaysis/',views.analysisview,name='analysis'),
  path('register/' , views.registerview,name='register'),
  path('complain/',views.complains,name = 'complain'),
  path('',views.logged,name='login')

] 