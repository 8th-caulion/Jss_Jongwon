from django.urls import path
from main import views
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('signup', views.signup, name="signup"),
    path('login', LoginView.as_view() , name="login"),
    path('logout', LogoutView.as_view() , name="logout"),
]


