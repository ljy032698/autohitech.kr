from django.urls import path

from . import views

app_name = 'downloads'

urlpatterns = [
    path('', views.index),
    path('<int:board_id>/', views.detail),
]