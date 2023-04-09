from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from socket import gethostname
from django.conf.urls import handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("product.urls")),
    path('', include("users.urls")),
    path('', include("post.urls")),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
