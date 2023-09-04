from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.twitter_login, name='login'),
    path('logout/', views.twitter_logout, name='logout'),
    path('complete/twitter/', views.twitter_auth_complete, name='twitter-auth-complete'),
]
