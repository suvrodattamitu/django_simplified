from django.urls import path
from .views import product_detail_view,product_create_view,product_dynamic_view,product_delete_view,product_list_view

app_name = 'products'

urlpatterns = [

	#path('',product_list_view, name='home'),
    path('<int:my_id>/',product_dynamic_view,name='product-detail'),
    path('<int:my_id>/delete/',product_delete_view,name='product-delete'),
    path('lists/',product_list_view),
    path('create/',product_create_view),
    path('',product_detail_view),

]
