from django.urls import path
from django.conf.urls import url
from list import views


urlpatterns = [
    url(r'festival/', views.findex),
    url(r'contest/', views.cindex),
]
   
