from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('atc-sda/', views.atcsda),
    path('atc-sdae/', views.atcsdae),
    path('atw-01/', views.atw01),
    path('atw-02/', views.atw02),
]