from django.urls import path
from . import views

urlpatterns = [
     path('', views.get_courses),
     path('<slug:slug>/', views.get_course)
 ]