from django.urls import path
from rest_framework.authtoken import views as account_view
from account import views

urlpatterns = [
    path('login/',account_view.obtain_auth_token, name = "login"),
    path('register/',views.UserRegistrationView.as_view(),name="register"),
    path('information/',views.InformationView.as_view(), name="information"),
]