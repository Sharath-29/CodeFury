from django.urls import path
from . import views 

urlpatterns = [
    path('home/', views.homes, name='homes'),
    path('<str:room>/', views.room, name='room'),
    path('home/checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>', views.getMessages, name='getMessages'),
]