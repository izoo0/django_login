from django.urls import path
from . import views


urlpatterns = [
     path('',views.home_view, name="home"),
     path('userlogin/',views.login_auth ,name="login-user"),
]
