from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls', namespace="core")),
    path('usuarios/', include('apps.accounts.urls', namespace="accounts")),
    path('escola/', include('apps.school.urls', namespace="school"))
]
