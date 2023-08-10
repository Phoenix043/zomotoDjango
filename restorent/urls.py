from django.urls import path
from . import views

app_name = "zomotoApp"

urlpatterns = [
   
    path('menu/add/', views.add_item_to_menu, name='add_item_to_menu'),
    path('', views.show_menu, name='show_menu'),
    path('order/add/', views.order_item, name='order_item'),
    path('order/update/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('orders/', views.view_all_orders, name='view_all_orders'),
]
