from django.urls import path

from . import views

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('product/<int:pk>/', views.product, name='product')
]
