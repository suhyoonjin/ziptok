from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('user/', include('user.urls')),
    path('first/', include('first.urls')),
    path('admin/', admin.site.urls),
]