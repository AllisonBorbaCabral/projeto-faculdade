from django.urls import path
from locations.views.country import index

urlpatterns = [
    path('', index, name='index'),
]