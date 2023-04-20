from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views as api_views, urls as api_urls

router = routers.DefaultRouter()
router.register(r'files', api_views.FilesView, 'file')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/pdf/', include(api_urls)),
]
