from django.urls import path,include
from .views import register,LoginView,Logout


app_name='user'
urlpatterns = [
    path('register/',register,name='register'),
    path('login/',LoginView,name='login'),
    path('logout/',Logout,name='logout'),
]

