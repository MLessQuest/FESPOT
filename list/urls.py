from django.urls import path
from django.conf.urls import url
from list import views

urlpatterns = [
    path('festival/', views.festival_list),
    path('festival/<int:pk>/', views.festival_detail),
    path('contest_detail/', views.contest_list),
    path('contest/<int:pk>/', views.contest_detail),
   ]
