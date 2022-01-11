from django.urls import path
from . import views

urlpatterns = [
    path("uploadFile/", views.fileUpload)
]
