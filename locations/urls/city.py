from django.urls import path
from locations.views.city import index

urlpatterns = [
    path('', index, name='index'),
]