from django.urls import path

from course import views

urlpatterns = [
    path('', views.CourseView.as_view(), name='course'),

]