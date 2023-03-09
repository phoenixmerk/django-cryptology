# _*_coding:utf-8_*_
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", views.index, name="index"),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
