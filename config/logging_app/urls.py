from django.urls import path
from logging_app import views

urlpatterns = [
    path('',views.home_view,name='home')
]