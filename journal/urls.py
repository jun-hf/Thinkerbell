from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # home page
    path('logs/', views.log_list, name='log'), # log page
    path('log/<int:log_id>/', views.log, name='log')
]