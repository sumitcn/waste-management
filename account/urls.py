from django.urls import path , include
from . import views


app_name='account'

urlpatterns=[
  
  path('logout/',views.logoutview,name='logout'),
  path('register/' , views.registerview,name='register'),
  path('',views.logged,name='login')

] 