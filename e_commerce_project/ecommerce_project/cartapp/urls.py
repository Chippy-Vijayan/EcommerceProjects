from django.urls import path
from . import views
app_name='cartapp'
urlpatterns = [
    path('',views.Cart_Detail,name='Cart_Detail'),
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('delete/<int:product_id>/',views.cart_delete,name='cart_delete'),
]