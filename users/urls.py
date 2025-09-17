from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/bulk-upload/', views.bulk_user_upload, name='bulk_user_upload'),
    path('users/delete-company/', views.delete_company_data, name='delete_company_data'),
    path('users/delete-attendance/', views.delete_attendance_data, name='delete_attendance_data'),
    path('users/template/', views.download_user_template, name='download_user_template'),
    path('notifications/', views.notifications, name='notifications'),
]