from django.urls import path , include
from . import views
#from django.contrib.auth import views as auth_views

app_name='account'

urlpatterns=[
  path('index/',views.index,name='index'),
  path('logout/',views.logoutview,name='logout'),
  path('register/' , views.registerview,name='register'),
  path('login/',views.loginview,name='login')



] 