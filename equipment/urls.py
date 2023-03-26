from django.urls import path
from equipment import views

urlpatterns = [
    path('data/', views.data_list),
    path('status/', views.get_status),
    path('set_ip/', views.set_ip_address),
    path('toggle', views.toggle_relay)
]