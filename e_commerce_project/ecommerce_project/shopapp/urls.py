from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views
app_name='shopapp'
urlpatterns = [
    path('',views.allProductCat,name='allProductCat'),
    path('add_cat/', views.add_category, name='add_category'),
    path('add_prod/',views.add_product,name='add_product'),
    path('<slug:c_slug>/',views.allProductCat,name='products_by_category'),
    path('<slug:c_slug>/,<slug:product_slug>/', views.productDetail, name='productCategoryDetail'),

]