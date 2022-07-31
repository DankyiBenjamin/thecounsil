from django.urls import path,re_path
from . import views

from django.views.static import serve
from django.conf import settings

urlpatterns = [


    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    # change with the home page 
    path('', views.loginPage, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('register/',views.registerPage, name = 'register'),


    path('home/',views.home ,name= "home"),
    path('room/<str:pk>/', views.room ,name = "room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),


    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>', views.deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>', views.deleteMessage, name='delete-message'),
    

    path('update-user/', views.updateUser, name='update-user'),
    path('topics/', views.topicsPage, name='topics'),
    path('activity/', views.activityPage, name='activity'),


]