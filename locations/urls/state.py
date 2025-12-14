from django.urls import path
from locations.views.state import index

urlpatterns = [
    path('', index, name='index'),
]