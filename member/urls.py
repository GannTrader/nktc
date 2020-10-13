from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.signup, name='register'),
    path('login/', views.SiteLoginView.as_view(), name='login'),
    path('logout/', views.SiteLogoutView.as_view(), name='logout'),

    #change pass
    path('password-change/', views.SitePasswordChangeView.as_view(), name='password-change'),
    path('password-change/done', views.SitePasswordChangeDoneView.as_view(), name='password-change-done'),

    #reset pass
    path('password-reset/', views.SitePasswordResetView.as_view(), name='password-reset'),
    path('password-reset-done/', views.SitePasswordResetDoneView.as_view(), name='password-reset-done'),
    path('password-reset-confirm/<uidb64>/<token>/', views.SitePasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('password-reset-complete/', views.SitePasswordResetCompleteView.as_view(), name='password-reset-complete'),

    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('edit-profile/<int:pk>/', views.EditProfileView.as_view(), name='edit-profile'),
    path('active/<uidb64>/<token>/', views.activate, name='active'),
]