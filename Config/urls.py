from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('admin_panel.urls')),
    path('api/', include('api.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)