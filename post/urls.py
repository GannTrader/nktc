from django.urls import path

from post import views


urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    path('post/', views.PostListView.as_view(), name='post'),
    path('detail/<slug:slug>', views.PostDetailView.as_view(), name='detail'),

    path('cmt/<slug:slug>', views.CommentView.as_view(), name='cmt'),
    path('reply/<int:pk>', views.ReplyView.as_view(), name='reply'),

    path('robots.txt/', views.RobotsView.as_view()),
]