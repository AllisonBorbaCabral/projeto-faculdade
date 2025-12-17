from django.urls import path, include
from .urls import urlpatterns as ui_urls

urlpatterns = [
    path('', include((ui_urls, 'ui'))),
]