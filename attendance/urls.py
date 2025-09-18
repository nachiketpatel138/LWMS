from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_list, name='attendance_list'),
    path('upload/', views.upload_attendance, name='upload_attendance'),
    path('edit/<int:pk>/', views.edit_attendance, name='edit_attendance'),
    path('export/', views.export_attendance, name='export_attendance'),
    path('template/', views.download_attendance_template, name='download_attendance_template'),
    path('empty-template/', views.download_empty_attendance_template, name='download_empty_attendance_template'),
    path('upload-history/', views.upload_history, name='upload_history'),
    path('upload-progress/<str:session_id>/', views.upload_progress, name='upload_progress'),
]