from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetDoneView
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    # Главная страница со списком пользователей
    path('', views.index, name='index'),

    # Отдельная страница с информацией о пользователе
    path('users/<int:pk>/', views.user_detail, name='user_detail'),

    # Страница редактирования пользователя
    path('users/<int:pk>/edit/', views.user_edit, name='user_edit'),

    # Страница регистрации
    path('signup/', views.SignUp.as_view(), name='signup'),

    # Страница выхода из аккаунта
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),

    # Страница авторизации
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),

    # Страница сброса пароля
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='users/password_reset_form.html'),
        name='password_reset_form'
    ),

    path(
        'password_reset/done',
        PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html'),
        name='password_reset_done'
    ),

    # Страница смены пароля
    path(
        'password_change/',
        PasswordChangeView.as_view(
            template_name='users/password_change_form.html'),
        name='password_change_form'
    ),

    path(
        'password_change/done',
        PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html'),
        name='password_change_done'
    )
]
