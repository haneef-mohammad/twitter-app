from django.conf.urls import url
from TwitterApp import views
from django.urls import path

urlpatterns=[
    path('users/', views.UsersView.as_view()),
    path('tweets/', views.TweetsView.as_view()),

]