from django.urls import path
from . import views

urlpatterns = [
	path('', views.frontdoor, name="frontdoor"),
	path('logged/', views.logged, name="logged"),
    path('home/', views.emp1, name="home"),
    # path('2/', views.emp2, name="emp2"),
]
