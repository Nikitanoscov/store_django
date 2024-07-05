from django.contrib import admin
from django.urls import include, path

from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('goods.urls', namespace='goods'))
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
