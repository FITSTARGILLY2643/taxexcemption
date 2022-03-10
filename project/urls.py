from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('client.urls')),
    path('ncpwd/',include('ncpwd.urls')),
    path('moh/',include('moh.urls')),
    path('kra/',include('kra.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

