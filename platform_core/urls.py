from django.urls import path
from .views import page_view

urlpatterns = [
    path("<slug:slug>/", page_view),
]
