from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/v1/', include('notes.urls')),
    path('admin/v2/', include('listings.urls')),
    path('admin/api/', include('api.urls'))
]