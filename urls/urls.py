from django.contrib import admin
from django.urls import path
from .views import index_url_view, CreateUrlView

urlpatterns = [
    path('', CreateUrlView.as_view()),
    path('<str:short>/', index_url_view),
]
