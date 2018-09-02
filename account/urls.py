from django.urls import path , include
from . import views
#from django.contrib.auth import views as auth_views

app_name='account'

urlpatterns=[
  path('',views.home,name='home'),
  path('index/',views.index,name='index'),
  path('logout/',views.logoutview,name='logout'),
  path('register/' , views.registerview,name='register'),
  path('login/',views.logged,name='login')

] 