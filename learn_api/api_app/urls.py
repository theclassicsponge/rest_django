from django.urls import path
from api_app import views

urlpatterns = [
    path('api_app/', views.api_app_list),
    path('api_app/<pk>/', views.api_app_detail),
]