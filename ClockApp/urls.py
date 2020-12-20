from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('logs/', views.SysLogView.as_view(), name='logs'),
#    path('logs/', views.log_list, name='log_list'),
    path('ClockApp/log/<int:logid>/', views.log_detail, name='log_detail'),
#    path('ships/<str:shipname>/', views.ship_detail, name='ship_detail'),
#    path('ships/new', views.ship_new, name='ship_new'),
#    path('ships/new', views.ship_edit, name='ship_edit'),
#    path('ships/<str:shipname>/edit/', views.ship_edit, name='ship_edit'),
]
