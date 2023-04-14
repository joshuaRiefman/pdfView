from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("viewer/", include("viewer.urls")),
    path("admin/", admin.site.urls),
]
