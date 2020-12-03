from django.urls import path
from . import views

urlpatterns = [
	path('', views.frontdoor, name="frontdoor"),
	path('logged/', views.logged, name="logged"),
    path('home/', views.emp1, name="home"),
    path('logout/', views.logout_user, name="logout"),

    #ACCOUNT INFO
    path('account/', views.user_acct, name="acct"),

    #PAYROLL
    path('payroll/', views.payroll, name="payroll"),

    #PAYROLL LOGIN
    path('paylogin/', views.payroll_login, name="paylogin"),
]
