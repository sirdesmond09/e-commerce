from django.urls import path
from .views import dashboard, register, edit
from django.contrib.auth import views as auth_views #using django inbuilt authentoication views

app_name = 'account'

urlpatterns = [
    #user dashboard
    path('profile/', dashboard, name = 'dashboard'),
    
    #register user
    path('register/', register, name = 'register'),

    #login and logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    
    # change password urls
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    
    # reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    #edit profile
    path('edit/', edit, name='edit'),
]