from django.urls import path

from post import views


urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    path('post/', views.PostListView.as_view(), name='post'),
    path('robots.txt/', views.RobotsView.as_view()),
]