from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r"upload/(?P<filename>[^/]+)$", views.ViewUpload.as_view())
]
