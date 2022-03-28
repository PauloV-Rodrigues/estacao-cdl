from .views import *
from django.urls import path

app_name = "library"

urlpatterns = [
    path ('login/', loginPage, name="login"),
    path('logout/', logoutPage, name="logout"),
    path('register/form/', registerPage, name="register"),
    
    path('', BookList, name='home'),
    path('<slug:slug>/', BookDetail.as_view(), name='detail'),

    path('contact/form/', contactPage, name="contact"),
    path('profile/user/', profilePage, name="profile"),
]