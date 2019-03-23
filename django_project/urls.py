"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view,contact_view,about_view,blog_view

#for raw
#from products.views import product_detail_view,product_create_view
#for pure django form
from products.views import product_detail_view,product_create_view,product_dynamic_view,product_delete_view,product_list_view

urlpatterns = [
	path('',home_view, name='home'),
	path('contact/',contact_view),
	path('about/',about_view),
    path('blog/',blog_view),
    path('product/',product_detail_view),
	path('create/',product_create_view),
    path('admin/', admin.site.urls),
    path('product/<int:my_id>/',product_dynamic_view),
    path('product/<int:my_id>/delete/',product_delete_view),
    path('product/lists/',product_list_view),
]
