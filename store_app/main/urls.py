from django.urls import path

from .views import about, index

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about')
]
