from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('login/', views.LoginView.as_view(), name="login"),
    path('profile/', views.ProfilePage.as_view(), name="profile"),
    path('register/', views.RegisterView.as_view(), name='register')
]