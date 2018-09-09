from django.urls import path , include
from . import views


app_name='waste'

urlpatterns=[
  
  path('complain/',views.complainview,name='complain'),
  path('submit/',views.submit,name='submit'),


] 