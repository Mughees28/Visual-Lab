from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.loginpage, name="login"),
    path('logout/',views.logoutuser, name="logout"),
    path('register/',views.registerpage, name="register"),
    path('',views.home, name='home'),
    path('room/<str:pk>/',views.room, name='room'),
    path('profile/<str:pk>/',views.userprofile, name='user-profile'),
    path('create-room/',views.createroom, name='createroom'),
    path('update-room/<str:pk>/',views.updateroom, name='updateroom'),
    path('delete-room/<str:pk>/',views.deleteroom, name='deleteroom'),
    path('delete-message/<str:pk>/',views.deletemessage, name='delete-message'),
    path('update-user/',views.updateuser, name='update-user'),
    path('topics/',views.topicsPage, name='topics'),
    path('activity/',views.activityPage, name='activity'),
    
]