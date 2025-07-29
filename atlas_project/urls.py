from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static


# تنظیمات مستندسازی
schema_view = get_schema_view(
   openapi.Info(
      title="Atlas API",
      default_version='v1',
      description="مستندات API پروژه اطلس",
      terms_of_service="https://www.atlas-aim.com/terms/",
      contact=openapi.Contact(email="info@atlas-aim.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),

    # مسیر مستندات
    re_path(r'^api/docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^api/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/v1/', include('api.urls')),  # Versioning API (نسخه‌بندی)

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)