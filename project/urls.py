from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('client.urls')),
    path('ncpwd/',include('ncpwd.urls')),
    path('moh/',include('moh.urls')),
    path('kra/',include('kra.urls')),
]
