# _*_coding:utf-8_*_
from django.contrib import admin

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("clipher",views.clipher,name="clipher"),
]
