from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # home page
    path('logs/', views.log_list, name='log'), # log page
    path('log/<int:log_id>/', views.log_detail, name='log_detail'),
    path('new_log/', views.new_log, name='new_log'),
    path('new_entry/<int:log_id>/', views.new_entry, name='new_entry')
]