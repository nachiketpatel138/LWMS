from django.urls import path
from . import views

urlpatterns = [
    # API endpoints
    path('api/login/', api_views.login_api, name='api_login'),
    path('api/dashboard/', api_views.dashboard_api, name='api_dashboard'),
    
    # Keep original views for now
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
]