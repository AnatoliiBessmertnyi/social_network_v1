from django.urls import patj

from . import views

urlpatterns = [
    path('', views.index),
    path('group/<slug:slug>/', views.group_posts()),
]